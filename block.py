import json
import os
import hashlib
import datetime


BLOCKCHAIN_DIR = "blockchain/"
##getting hash of block
def get_hash(previous_block):
    with open (BLOCKCHAIN_DIR+ previous_block, 'rb') as f:
        content = f.read()
    return hashlib.md5(content).hexdigest()


##This is a method to check whether a block is shanged or not, any changed block will result in an error as blocks are not allowed to br modified
def check_integrity():
    ##getting hash of each block
    #start from second block as first one has no hash
    files = sorted(os.listdir(BLOCKCHAIN_DIR), key=lambda x: int(x))
    results = []

#a for loop to load the blocks
    for file in files[1:3]:
        with open(BLOCKCHAIN_DIR + file) as f:
            block = json.load(f)
##getting the block previous hash
        prev_hash = block.get('previous_block').get(hash)
        prev_filename = block.get('previous_block').get('filename')

        actual_hash = get_hash(prev_filename)

        if prev_hash == actual_hash:
            res = 'ok'
        else:
            red = 'not ok'

        print(f'Block {prev_filename}: {res}')
        results.append({'block': prev_filename, 'result':res})
    return results
##this method is responsible for creating new blocks
def write_block(data, timestamp):

    blocks_count = len( os.listdir(BLOCKCHAIN_DIR))
    previous_block = str(blocks_count)
    timestamp=str(datetime.datetime.now())


##data that should be in each block
    data_of_block = {
        "data":data,
    'timestamp': timestamp,
    "previous_block":{
        "hash":get_hash(previous_block),
        "filename":previous_block,
        

    } 
    }

    current_block = BLOCKCHAIN_DIR + str(blocks_count) +1
    with open(current_block, 'w') as f:
        json.dump(data_of_block, f, indent=3, ensure_ascii=False)
        f.write('/n')

def main():
    check_integrity()

if __name__=='__main__':
    main()
