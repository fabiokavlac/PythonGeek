from datetime import datetime

data = datetime.now()
atual = data.strftime("%d/%m/%Y, %H:%M:%S")
print(f'A data e hora atual de hoje é: \n{atual}')

import datetime
now = datetime.datetime.now()
print("current date and time : ")
print(now.strftime("%Y-%m-%d %H:%M:%S"))


from datetime import datetime

## In your route...

now = datetime.now() # current date and time
date_time = now.strftime("%d/%m/%Y, %H:%M:%S")

return render_template('date-time.html', date_time=date_time)

## In your Jinja template...

<p>The date and time is: {{ date_time }}</p>