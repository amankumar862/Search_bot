from flask import Flask, render_template, request
import wikipedia

app = Flask(__name__)

def search_wiki(query):
    wikipedia.set_lang('en')
    try:
        search_results = wikipedia.search(query, results = 5)
        if not search_results:
            return 'No Information found'
        
        meanings = []
        for result in search_results:
            try:
                summary = wikipedia.summary(result, sentences = 2)

                #meanings.append(f"*{result}* - {summary}")
                
                url = f"https://en.wikipedia.org/wiki/{result.replace(' ','_')}"

                meanings.append({
                    "title": result,
                    "summary": summary,
                    "url": url
                })

            except wikipedia.exceptions.DisambiguationError:
               meanings.append({
                   "title": result,
                   "summary":"Multiple meanings available",
                   "url":f"https://en.wikipedia.org/wiki/{result.replace(' ','_')}"
               })

            except wikipedia.exceptions.PageError:
                continue

        return meanings
    
    except Exception as e:
        return f"Error: {e}"
    
#query = input("Enter search text: ")
#print("\n Results:\n", search_wiki(query))

@app.route("/", methods=["GET", "POST"])
def index():

    result = ""

    if request.method == "POST":
        query = request.form["search"]
        result = search_wiki(query)
    
    return render_template("index.html", result = result)

if __name__ == "__main__":
    app.run(debug = True)
