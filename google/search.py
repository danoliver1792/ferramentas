from googlesearch import search

query = 'python'

result = list(
    search(
        query,
        lang='pt-br',
        num_results=5
    )
)

print(result)
