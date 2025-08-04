def write_to_file(filename,content):
    with open(filename,'w') as f:   #creates a file, w stands for write
      f.write(content)

if __name__ == "__main__":
    write_to_file('output.txt','Hello from python script!')
    print("File is created and content written")