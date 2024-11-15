'''guess a number game'''

from random import randint

class Player:
    
    def __init__(self):
        self.name = input('Insert your name: ')
        self.counter = 0
        
        
    def guess(self):
        try:
            self.num = int(input('Guess a number between 1 to 100:'))
        except:
            self.counter += 1 
        
        
class Game:
        
        def __init__(self):
            self.num = randint(1, 100)
            self.player = Player()
            self.playing()
            
        def playing(self):
            
            while self.player.counter <= 10:
                self.player.guess()
                if self.player.num == self.num:
                    print(f'Congrats! {self.player.name} Your number {self.player.num} is same like guessed number')
                    
                elif self.player.num < self.num:
                    print(f'=== Your number is lower === \nThis is your attempt number  {self.player.counter}. Try it again! \n')
                    
                else:
                    print(f'=== Your number is upper === \nThis is your attempt number {self.player.counter}. Try it again! \n' )
            
            if self.player.counter > 10:
                print('Sorry {self.player.name}, but you lose!')
                yes_no = input('Do you want to play again? yes/no').lower()
                if yes_no == 'yes':
                    Game()
                else:
                    print('Okey, see you.')
                
                
Game()
         
        