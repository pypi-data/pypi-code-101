# import iap_token
# import os

# def test_no_tracking_uri():
#     id_token = iap_token.get_token("")
#     assert id_token == None
#     # print(iap_token.get_token(os.environ["MLFLOW_TRACKING_URI"]))

# def test_google_cloud_login():
#     id_token = iap_token.get_token("https://console.cloud.google.com")
#     assert id_token != None
#     # print(iap_token.get_token(os.environ["MLFLOW_TRACKING_URI"]))

# if __name__ == "__main__":
#     test_logging()
