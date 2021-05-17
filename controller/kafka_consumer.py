from kafka import KafkaConsumer

last=[]
consumer = KafkaConsumer('water',
                         group_id='group-in',
                         bootstrap_servers=['121.196.54.227:9092'])
print("????")
for message in consumer:
    # message.value的字节形式：['b\'1','2018-01-01 00:00:00','6.93','9.03',....,'0\'']
    print(message.value)
    curr = {'time': str(message.value).split(',')[1],
            'value': str(message.value).split(',')[2]}
    last.append(curr)
