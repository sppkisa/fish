import time

from kafka import KafkaProducer

if __name__ == '__main__':

    producer = KafkaProducer(bootstrap_servers=['121.196.54.227:9092'])
    with open('C:\\Users\\sankoo\\Desktop\\lunwen\\origin_ano_short.csv', 'r') as f:
        count = 0
        for line in f:
            producer.send('water', line.rstrip().encode())
            print("推送一条：成功！")
            time.sleep(0.2)
            count += 1
        producer.flush()
