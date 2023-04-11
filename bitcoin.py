import sys
import requests

def main():
    while True:
        try:
            coins = float(sys.argv[1])
            total = get_price(coins)
            total = '{:,.4f}'.format(total)
            print(f'${total}')
            break
        except ValueError:
            if len(sys.argv)==1:
                sys.exit('Missing Command-line argument')

            sys.exit('Command-line argument is not a number')


def get_price(coins):

    try:
        r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        p = r.json()
        p = p['bpi']['USD']['rate']
        p = p.replace(',','')
        p = float(p)
        total = coins * p
        return total
    except requests.RequestException:
        sys.exit()


main()



