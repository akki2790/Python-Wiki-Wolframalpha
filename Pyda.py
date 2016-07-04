import wolframalpha

input = raw_input("Question: ")
app_id = "YHUEYQ-AE59WVTVEG"
client = wolframalpha.Client(app_id)

res = client.query(input )
answer = next(res.results).text

print answer
