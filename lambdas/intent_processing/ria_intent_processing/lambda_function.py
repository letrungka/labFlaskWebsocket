import logging
import json
import os

import boto3
from pythonjsonlogger import jsonlogger


DEFAULT_LOGLEVEL = 'DEBUG'

# ENV Values
ENVIRONMENT = os.getenv('RS_ENVIRONMENT')
LOGLEVEL = os.getenv('RS_LOGLEVEL', DEFAULT_LOGLEVEL)


# Setup logging
LOGGER = logging.getLogger()
LOGGER.setLevel(LOGLEVEL)
HANDLER = logging.StreamHandler()
HANDLER.setFormatter(jsonlogger.JsonFormatter())
LOGGER.addHandler(HANDLER)
LOGGER.removeHandler(LOGGER.handlers[0])

# minimize boto logging
logging.getLogger('boto3').setLevel(logging.CRITICAL)
logging.getLogger('botocore').setLevel(logging.CRITICAL)
logging.getLogger('s3transfer').setLevel(logging.CRITICAL)
logging.getLogger('urllib3').setLevel(logging.CRITICAL)


def dispatch(request):
    '''
    Dispatch
    Can be used to handle custom logic for individual intents. Once more complex
    Lex workflows are created, more custom logic will be needed.
    '''
    LOGGER.info('dispatching request')
    LOGGER.debug(request['currentIntent'].keys())

    intent = request['currentIntent']['name']
    response = build_simple_fulfillment_response('Well, Testing successfully !!!')

    return response


def build_simple_fulfillment_response(message=None):
    '''
    Builds a Simple Fulfillment Response
    DialogAction of type Close
    '''
    LOGGER.info('building simple fulillment response')

    response = {
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": "Fulfilled"
        }
    }

    # add message if provided - should be a string
    # to add additional more than a message pass a jsonify string
    if message is not None:
        response['dialogAction']['message'] = {'contentType': 'PlainText', 'content': message}

    LOGGER.debug(response)
    return response


def lambda_handler(event, context):
    LOGGER.info('processing event', extra={'event': event})
    return dispatch(event)
