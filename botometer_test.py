import botometer
import configparser


#read credential from config.ini

config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']
access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']
rapidapi_key = '45eb40eb4amsh498f5b60a9db3aep192d97jsnc5e0771aa412'

twitter_app_auth = {
    'consumer_key': 'a3ogMemAmtcQ9Ov8XbpPhPKKM',
    'consumer_secret': 'GodyLK9iBubMdLpRlXuiq3sO9L2BQ4Wn2BQNubsqH0XcsmhPBg',
    'access_token': '1578462726040555521-M8wYqTjgFSYdt9x4QrbSGyjlJ2WX6c',
    'access_token_secret': 'otys8T38E8haeM2J9op0gpyHhQ1OZzhvaPZLEd3oEgY2E',
  }
  
blt_twitter = botometer.BotometerLite(rapidapi_key=rapidapi_key, **twitter_app_auth)

# # Prepare a list of screen_names you want to check.
# # The list should contain no more than 100 screen_names; please remove the @
screen_name_list = ['principe_xia']
blt_scores = blt_twitter.check_accounts_from_screen_names(screen_name_list)

# # Prepare a list of user_ids you want to check.
# # The list should contain no more than 100 user_ids.
# user_id_list = [113306978091785]
# blt_scores = blt_twitter.check_accounts_from_user_ids(user_id_list)


print(blt_scores)