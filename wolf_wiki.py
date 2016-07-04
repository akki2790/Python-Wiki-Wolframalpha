
import wolframalpha

while True:
    input = raw_input("Q: ")

    try:
        app_id = "YHUEYQ-AE59WVTVEG"
        client = wolframalpha.Client(app_id)

        res = client.query(input )
        answer = next(res.results).text

        print answer
    except:
        print wikipedia.summary(input)
