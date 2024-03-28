from wasteDetection.logger import logging
from wasteDetection.pipeline.training_pipeline import TrainPipeline
logging.info("Welcome")

obj = TrainPipeline()
obj.run_pipeline()