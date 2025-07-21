print("Photo Gallery:")
data={
    1:"beach.jpg",
    2:"mountain.jpg",
    3:"party1.jpg",
    4:"selfile.jpg",
    5:"birthday.jpg",
    6:"concert.jpg",
    7:"sunset.jpg",
    8:"trip1.jpg"
}
for i in data :
    print(f'{i}. {data[i]}')

l = list(map(int,input("Select photos to share (enter numbers separated by comma):\nYour Selection :").split(',')))

print("Sharing the following photos:")
for i in l:
    print(f'{data[i]}')
