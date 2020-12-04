from config import SESSION_ID, USER_AGENT
import os
import time
from urllib import request

def get_data():
    
    # setup
    print('Getting data for Advent of Code...')
    time.sleep(1)
    year = input('What year is it? ')
    day = input('What day is it? ')
    choice = input(f'Pull data for {year}: {day}? (y/n) ')
    
    # request
    if choice == 'y':
        uri = 'http://adventofcode.com/{year}/day/{day}/input'.format(year=year,day=day)
        
        # config req
        session = f'session={SESSION_ID}'
        req = request.Request(
            uri,  
            headers={'Cookie': session, 'User-Agent':USER_AGENT}
        )
        
        # open/decode
        response = request.urlopen(req).read().decode('utf-8')

        # make dir
        print('Writing file...')
        path = f'day_{day}'
        os.makedirs(path)
        
        # write file
        with open(f'{path}/input.txt','w') as file:
            file.write(response)
            file.close()
        
        # python script
        try:
            open(f'{path}/puzzle.py', 'x').close()
        except FileExistsError:
            ('.py already exists')
            pass
        print('Job done!')
    
    else:
        print('Exiting.')

if __name__ == '__main__':
    exit(get_data())