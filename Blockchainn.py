import hashlib
import datetime
import base64
# from pyCrypto import Random
# from Crypto.Cipher import AES


# BS = 16
# pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
# unpad = lambda s: s[0:-ord(s[-1])]

# class AESAlgorithm:
#     def __init__( self):
#         pass
#     def encrypt( self, message, symmetricKey):
#         raw = pad(message)
#         symmetricKey = hashlib.sha256(symmetricKey.encode('utf-8')).digest()
#         iv = Random.new().read( AES.block_size)
#         cipher = AES.new( symmetricKey, AES.Mode_CBC, iv)
#         return base64.b64encode(iv + cipher.encrypt( raw ))

#     def decrypt( self, enc, symmetricKey):
#         enc = base64.b64secode(enc)
#         symmetricKey = hashlib.sha256(symmetricKey.encode('utf-8')).digest()
#         iv = enc[:16]
#         cipher = AES.new(symmetricKey, AES.MODE_CBC, iv)
#         return unpad(cipher.decrypt( enc[16:] ))


# AESAlgorithm = AESAlgorithm()

# plaintext="hello guys"
# symKey1 = "1234"
# encryptedText = AESAlgorithm.encrypt(plaintext, symKey1)
# print(encryptedText)


##First Class
class block:
    ##block format
    def __init__(self, previous_block_hash, timeStamp, data):
        self.previous_block_hash = previous_block_hash
        self.timestamp = timeStamp
        self.data = data
        self.chain = []
        # self.generate_blocks()

        ## Appending all data in block_data
        self.block_data = "-" .join(data) + "-" + timeStamp + "-" + previous_block_hash

        ## Hashing the block
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()
        
    def generate_blocks(self):

          new_block= block(data=input('data:   '), timeStamp=str(datetime.datetime.now()))
          self.chain.append(new_block)
        
          return new_block
        

##Testing for block one, no previous hash
t1 = "first"
t2 = "second"
t3 = "3rd"
data="123456789"
timestamp=str(datetime.datetime.now())
# timestamp= datetime.date.today().strftime("%H:%M:%S")
initial_block = block(data, timestamp, [t1, t1])

print(initial_block.block_data)
print(initial_block.block_hash)

##Hashing is working, if something is changed in the input, then the hashing will change.

##Testing for any other block, hashing of the previous block exists
secondBlock = block(timestamp, initial_block.block_hash, data)
print(secondBlock.block_data)
print(secondBlock.block_hash)

