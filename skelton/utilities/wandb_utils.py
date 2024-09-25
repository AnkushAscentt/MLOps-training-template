import logging
import os

import joblib
import wandb


def wandb_logging(
    entity_name, project_name, model_registry, flag, MODEL_FILENAME, train_score, test_score, model
):

    if flag == True:
        # Setup logger
        logger = logging.getLogger(__name__)

        logger.info("wandb connection start\n")

        wandb.init(entity=entity_name, project=project_name)

        # Resume the run with the same ID
        wandb.log({"Training Score": train_score, "Test Score": test_score})

        # Model registry
        joblib.dump(model, MODEL_FILENAME)

        # Create an artifact
        artifact = wandb.Artifact("trained-model", type="model")
        logger.info("done wandb artifact\n")

        # Add the model file to the artifact
        artifact.add_file(MODEL_FILENAME)
        logger.info("done wandb artifact add\n")

        # Log the artifact to the W&B run
        wandb.log_artifact(artifact)
        logger.info("done wandb artifact log\n")

        # Link the artifact to the model registry

        wandb.run.link_artifact(artifact, f"{entity_name}/{project_name}/{model_registry}")
        logger.info("done with wandb model registry\n")
        wandb.run.finish()
    else:
        run = wandb.init(entity=entity_name, project=project_name)


# Example usage:
# wandb_logging("your_entity_name", "your_project_name", train_score, test_score, your_model, run_id)
