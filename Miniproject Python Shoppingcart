#Python miniproject SHOPPINCART:
class shoppingcart:
    shopname='Flipcart'
    Delivery='Free shiping'
    item={'mobile':[8,10000],'watch':[5,1000],'laptop':[5,25000],'TV':[2,20000]}
    def __init__(self,name,phno,address,cart):
        self.name=name
        self.phno=phno
        self.address=address
        self.cart=cart
    def yourdetails(self):
        print(f'name:{self.name}')
        print(f'phno:{self.phno}')
        print(f'address:{self.address}')
        print(f'cart:{self.cart}')
    @classmethod
    def product_creat(cls):
        p1.cart[c]=[quantity,p1.item[c][1]*quantity]
        cls.item[c]=[p1.item[c][0]-quantity,p1.item[c][1]]
    def product_update(cls):
         cls.item[c]=[p1.item[c][0]-quantity,p1.item[c][1]]
         p1.cart[c]=[quantity+p1.cart[c][0],p1.cart[c][1]+p1.item[c][1]*quantity]
    @classmethod
    def removeproduct(cls):
        cls.item[R]=[p1.item[R][0]+H,p1.item[R][1]]
        p1.cart[R]=[p1.cart[R][0]-H,p1.cart[R][1]-p1.item[R][1]*H]
    
p1=shoppingcart('praba',8778828170,395,{})

        
    
while True:
      print('''WELCOME:   ENTER 1 TO DISPLAY ALL THE PRODUCTS AVAILABLE IN THE SHOP
           ENTER 2 TO DISPLAY ALL YOUR DETAILS
           ENTER 3 ADD PRODUCT INTO THE CART
           ENTER 4 TO REMOVE PRODUCT FROM THE CART
           ENTER 5 TO EXIT''')
      print('--------Hey buddies welcome to shopingcart---------')
      a=int(input('Enter the number:'))
      if a==5:
          print('THANKS YOU TATA BAYEE BAYEE')
          break
      elif a==1:
        print('product:[qty,price]\nmobile:',p1.item.get('mobile'),'\nwatch: ',p1.item.get('watch'),'\nlaptop:',p1.item.get('laptop'),'\nTv:    ',p1.item.get('TV'))
      elif a==2:
        p1.yourdetails()
      elif a==3:
          print('What product you add sir?')
          c=input('Enter the product:')
          if c in p1.item.keys():
              print('How many quantity')
              quantity=int(input('Enter the quantity:'))
              if quantity <= p1.item[c][0] :
                  print('Quantity is  available')
                  if c in p1.cart:
                      p1.product_update()
                      print('Product added successfully')
                  else:
                      p1.product_creat()
              else:
                   print('quantity is not available only left',p1.item[c][0])
          else:
             print('This item is not available') 
      elif a==4:
          print('To remove the product from the cart')
          if p1.cart == {}:
              print('No product available in this cart')
          else:
               R=input('Enter the product to remove:')
               if R in p1.cart:
                   H=int(input('How many product remove:'))
                   if H<=p1.cart[R][0]:
                       p1.removeproduct()
                       print('The product is removed')
                       if p1.cart[R][0]==0:
                           p1.cart.pop(R)
                           print('Product is removed successfully')
                   else:
                          print(p1.cart[R][0],'only this quantity is available')
               else:
                    print('This product is not available in the cart')
    
      
    
       
           

        
                        
