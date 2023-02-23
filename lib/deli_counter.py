# Practice building functions that use iteration and controlling their return values
# Practice manipulating lists (adding elements, removing elements, etc.)

katz_deli = []
# katz_deli = ['mary', 'jim', 'rob']

def line(katz_deli):

     if not katz_deli:
          print('The line is currently empty.')
     else:
          msg = 'The line is currently:'
          # While Loop:
          i = 0
          while i < len(katz_deli):
               msg += f' {i + 1}. {katz_deli[i]}'
               i += 1
          # For Loop:
          # for i in range(len(katz_deli)):
          #      msg += f' {i + 1}. {katz_deli[i]}'
               # if you don't surround katz_deli[i] with {} you won't get its value
          
          print(msg)
     
def take_a_number(katz_deli, customer):
     katz_deli.append(customer)
     print(f'Welcome, {customer}. You are number {len(katz_deli)} in line.')

def now_serving(katz_deli):
     if not katz_deli:
          print('There is nobody waiting to be served!')
     else:
          print(f'Currently serving {katz_deli[0]}.')
          del katz_deli[0]
     
