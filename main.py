import argparse

def add_argument():
    parser = argparse.ArgumentParser(description="analyze text")
    parser.add_argument("filename", help="The file to analyze")
    parser.add_argument("-s","--search", help="Text to search for")
    
    return parser.parse_args()

def main():
    try:
        args = add_argument()
        with open(args.filename, "rt") as file_toread: #open file
            content = file_toread.read()#closed
        
        # Count numbers of line
        lines = content.splitlines()
        lines_count = len(lines)
        
        # Count numbers of characters
        char_count = len(content.replace("\n", ""))
        
        # Split words and clean them(excluding punctuation marks)
        words = content.split()
        word_cleaned = ["".join(char for char in word if char.isalpha())for word in words]
        word_cleaned = [word for word in word_cleaned if word]
        total_word = len(word_cleaned)
        
        # Count numbers of unique words (case insensitive)
        unique_words = set(word.lower() for word in word_cleaned)
        unique_words_count = len(unique_words)
        
        # Results
        print("filename: ", args.filename)
        print("word searching for: ", args.search)
        print("Total lines: ", lines_count)
        print("Total characters: ", char_count)
        print("Unique words: ", unique_words_count)
        print("numbers of total words: ", total_word) #num
        
        # Keyword search
        word_count = 0 #counter
        if args.search:
            keyword = args.search.lower()
            for word in word_cleaned:
                if word.lower() == keyword:
                    word_count += 1 
        # Keyword search result
        print("Keyword occurrences: ", word_count)
    
    except FileNotFoundError:
        print("Error: File ", args.filename, " not found")
    except Exception as e:
        print("Error: ", e)

if __name__ == "__main__":
    main()
