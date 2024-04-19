from db.model import session, User, Token
import os

async def createToken(token):
    item = Token(tok_address=token)
    session.add(item)
    session.commit()

async def readToken():
    tokens = session.query(Token).all()
    return tokens

async def deleteToken(token):
    session.query(Token).filter(Token.tok_address == token).delete()
    session.commit()

async def createUser():
    hash = os.urandom(15).hex()
    item = User(user_address= hash, user_balance=0.000, user_announcement = False, user_auto_buy = False, min_pos_value =0.01, slippage_buy = 10, slippage_sell = 10)
    session.add(item)
    session.commit()

async def deleteUser():
    user = session.query(User).first()
    session.delete(user)
    session.commit()

async def readUser():
    user = session.query(User).first()
    return user


async def updateUser(user_balance = None, user_announcement = None, user_auto_buy = None, min_pos_value = None, slippage_buy = None, slippage_sell = None):
    user = session.query(User).first()
    if(user_balance != None):
        user.user_balance = user_balance
    if(user_announcement != None):
        user.user_announcement = user_announcement
    if(user_auto_buy != None):
        user.user_auto_buy = user_auto_buy
    if(slippage_buy != None):
        user.slippage_buy = slippage_buy
    if(slippage_sell != None):
        user.slippage_sell = slippage_sell
    if(min_pos_value != None):
        user.min_pos_value = min_pos_value
    
    session.commit()