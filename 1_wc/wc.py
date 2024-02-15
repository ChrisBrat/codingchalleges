import sys, getopt
import fileinput

def get_file_bytes(lines):
   count = 0
   for line in lines:
      count += sys.getsizeof(line)
   return count

def get_file_lines(lines):
   return len(lines)

def get_file_words(lines):
   count = 0
   for line in lines:
      words = line.split()
      words = [x for x in words if x != '\n' and x != '']
      count += len(words)
   return count

def get_file_characters(lines):
   count = 0
   for line in lines:
      count += len(line)
   return count

def main(argv):
    try:
      lines = []
      
      stream = not sys.stdin.isatty()

      if stream:
         lines = get_lines_from_stdin()
         opt, filename = get_opts(argv, stream)
      else :
         opt, filename = get_opts(argv, stream)
         lines = get_lines_from_file(filename)

      results = []
      if opt == '-l' or opt == None:
         results.append(get_file_lines(lines))
      if opt == '-w' or opt == None:
         results.append(get_file_words(lines))
      if opt == '-c' or opt == None:
         results.append(get_file_bytes(lines))
      if opt == '-m':
         results.append(get_file_characters(lines))
      
      print(("".join([str(result).rjust(8) for result in results]))+(" "+filename if filename != None else ""))   
    except getopt.GetoptError as error:
      print(f'Error {error}')
      sys.exit()

def get_lines_from_file(filename):
   lines = []
   try:
      if filename != None:
         with open(filename,'r',encoding="utf8") as file :
            for line in file:
               lines.append(line)         
   except Exception as error:
      print(f"Error opening file {filename} : {error}")
      sys.exit()
   return lines


def get_lines_from_stdin():
   lines = []
   try:   
      with fileinput.input(encoding="utf-8") as f:
         for line in f:
            current_line = line.strip("\n")
            lines.append(current_line)
   except:
      pass
   return lines

def get_opts(argv, stream):
    (opt, filename) = (None, None)
    opts, args = getopt.getopt(argv, "hclwm" if stream else "hc:l:w:m:")
    if len(opts) > 0:      
       (opt, filename) = opts[0] 
    elif len(args) > 0:
       (opt, filename) = (None,args[0])
    return opt,filename

if __name__ == "__main__":
    main(sys.argv[1:])