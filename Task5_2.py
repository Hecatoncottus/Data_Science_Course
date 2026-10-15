queries_input = input("Введите поисковые запросы через запятую: ")
raw_queries = queries_input.split(',')
search_queries = []

for query in raw_queries:
    
    clean_query = query.strip()
    
    if clean_query:
        
        search_queries.append(clean_query)


def get_word_distribution(queries):
    
    if len(queries) == 0:
        print("Список запросов пуст.")
        return

    total_count = len(queries)
    word_counts = {}

    for query in queries:
        
        words_count = len(query.split())
        
        if words_count in word_counts:
            
            word_counts[words_count] += 1
            
        else:
            word_counts[words_count] = 1

    sorted_keys = sorted(word_counts.keys())
    print("Распределение поисковых запросов:")

    for key in sorted_keys:
        
        count = word_counts[key]
        percentage = round((count / total_count) * 100, 2)
        print(f"{key} слов : {percentage}%")

get_word_distribution(search_queries)