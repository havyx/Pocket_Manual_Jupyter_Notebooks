import multiprocessing

#print(multiprocessing.cpu_count())

def spawn(num):
  print(num)

if __name__ == '__main__':
  for i in range(25):
    ## right here
    p = multiprocessing.Process(target=spawn, args=(i,))
    p.start()
    p.join()