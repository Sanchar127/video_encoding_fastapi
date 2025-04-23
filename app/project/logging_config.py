import logging

# Configure logger
def setup_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    
    # Create a console handler for output to stdout
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    
    # Create formatter and attach it to the handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    
    # Add the handler to the logger
    logger.addHandler(ch)
    
    # Optionally, log to a file
    file_handler = logging.FileHandler('app.log')
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
