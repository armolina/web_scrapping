import uuid

def request_log(start_date, end_date, web_scrapered, payload):
    request_log_dict = {
        'uuid': str(uuid.uuid1()),
        'start_date': start_date,
        'end_date': end_date,
        'web_scrapered': web_scrapered,
        'object_type': "href",
        'number_objetcs': len(payload),
        'payload': payload
    }
    return request_log_dict
