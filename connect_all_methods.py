import record
import speech_to_text
from access_ai import call_chatgpt3
import json

from privacy import remove_names

# sample to test:
"""
text = "Bitte fassen Sie diesen Dialog in Stichpunkten zusammen:\n" \
         "Doktor: Guten Morgen, wie kann ich Ihnen heute helfen?\n" \
         "Patient: Hallo, ich habe seit einiger Zeit Schmerzen in der Brust und bin kurzatmig.\n" \
         "Arzt: Okay, lassen Sie mich damit beginnen, einige Hintergrundinformationen von Ihnen zu erhalten. Wie heißen Sie und wie alt sind Sie?\n" \
         "Patient: Mein Name ist John, und ich bin 45 Jahre alt.\n" \
         "Doktor: Vielen Dank, John. Hatten Sie schon einmal Brustschmerzen oder Kurzatmigkeit?\n" \
         "Patient: Nein, das ist das erste Mal.\n " \
         "Arzt: Okay, können Sie mir die Schmerzen in der Brust beschreiben? Ist es ein scharfer Schmerz, ein dumpfer Schmerz oder etwas anderes?\n" \
         "Patientin: Es ist ein scharfer Schmerz in der Mitte meiner Brust.\n" \
         "Arzt: Und was ist mit der Kurzatmigkeit? Wann tritt sie auf, und wie stark ist sie?\n" \
         "Patientin: Ich merke es, wenn ich etwas Aktives tue, zum Beispiel gehen oder Treppen steigen. Sie ist ziemlich stark, und ich muss anhalten und nach Luft schnappen.\n" \
         "Arzt: Haben Sie noch andere Symptome, wie Schwitzen, Übelkeit oder Schwindelgefühl?\n" \
         "Patient: Nein, nur die Schmerzen in der Brust und die Kurzatmigkeit.\n" \
         "Arzt: Gut, haben Sie in letzter Zeit irgendwelche Medikamente eingenommen oder wurden Sie operiert?\n" \
         "Patientin: Nein, ich bin nicht operiert worden und nehme auch keine Medikamente ein.\n" \
         "Arzt: Okay, danke für diese Information. Gibt es in Ihrer Familie eine Vorgeschichte von Herzerkrankungen?\n" \
         "Patient: Ja, mein Vater hatte einen Herzinfarkt, als er 50 Jahre alt war.\n" \
         "Arzt: Das ist wichtig zu wissen. Aufgrund Ihrer Symptome und Ihrer Familiengeschichte sollten wir einige weitere Tests durchführen. Ich würde gerne ein Elektrokardiogramm (EKG) und eine Blutuntersuchung ansetzen, um eventuelle Herzprobleme festzustellen. Wäre das für Sie in Ordnung?\n" \
         "Patientin: Ja, natürlich.\n" \
         "Arzt: Sehr gut. Ich werde eine Überweisung für diese Tests ausstellen, und dann werden wir weitermachen. In der Zwischenzeit sollten Sie sich schonen und anstrengende Aktivitäten vermeiden, bis wir herausgefunden haben, was los ist."
"""


def assemble_ai_query(query_for_ai):
    if query_for_ai == "Protocol (Report)":
        return "Fasse diesen Dialog in einen Schreiben zur Dokumentation zusammen. Wichtig keine zusätzlichen Informationen, " \
               "alle Symptome und Diagnosen und der Behandlungsplan falls vorhanden sollen enthalten sein. Wen die Inforamtion " \
               "im Dialog fehlt schreib das das im Gespräch nicht erwähnt wurde. :"
    elif query_for_ai == "Letter to Patient":
        return "Fasse diesen Dialog zu einem Schreiben für den Patienten zusammen. Wichtig keine zusätzlichen Informationen, " \
               "alle Symptome und Diagnosen und der Behandlungsplan falls vorhanden sollen enthalten sein. Wen die Inforamtion " \
               "im Dialog fehlt schreib das das im Gespräch nicht erwähnt wurde. : "
    else:
        return "Fasse diesen Dialog in Stichpunkte zusammen, nur die medizisch relevanten Inforamtionen:"


def do_the_work(name_remove, query_for_ai, new_record):
    # Open the file in read mode
    with open('confiq.json', 'r') as file:
        # Load the contents of the file as a Python object
        data = json.load(file)
        filename = data['FILENAME']
        api_key = data['API_KEY']
        max_tokens = data['MAX_TOKENS']
        record_time = data['RECORD_TIME']
    order_for_ai = assemble_ai_query(query_for_ai=query_for_ai)
    if new_record:
        print("Theoretical a new record")
        record.record_function(filename=filename, record_time=record_time)
    text = order_for_ai + speech_to_text.start_speech_recognition(filename=filename)
    text = remove_names(name_remove, text)
    text = call_chatgpt3(api_key, text, max_tokens)
    return text
