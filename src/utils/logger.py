# Audit logging

import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_audit_event(event):
    logging.info(event)