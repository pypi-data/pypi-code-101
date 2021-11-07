PAGINATION_MODEL = {
    "list_job_executions_for_thing": {
        "input_token": "next_token",
        "limit_key": "max_results",
        "limit_default": 100,
        "page_ending_range_keys": ["jobId"],
    }
}
