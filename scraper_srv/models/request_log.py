import uuid

def request_log(start_date, end_date, web_scraper, object_type, payload):
    request_log_dict = {
        'uuid': str(uuid.uuid1()),
        'start_date': start_date,
        'end_date': end_date,
        'web_scraper': web_scraper,
        'object_type': object_type,
        'number_objetcs': len(payload),
        'payload': payload
    }
    return request_log_dict
