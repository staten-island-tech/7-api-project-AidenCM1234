import  requests
def test():
    response = requests.get('https://api.chess.com/pub/player/hikaru')
    print(response)
test()