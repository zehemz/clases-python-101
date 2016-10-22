import sqlite3
conn = sqlite3.connect('example.db')

c = conn.cursor()
# Never do this -- insecure!
symbol = 'RHAT'
c.execute("SELECT * FROM stocks WHERE symbol = '%s'" % symbol)

# Do this instead
t = ('RHAT',)
c.execute('SELECT * FROM stocks WHERE symbol=?', t)
print c.fetchone()

# Larger example that inserts many records at a time
purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
             ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
             ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
            ]
c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)


# >>> for row in c.execute('SELECT * FROM stocks ORDER BY price'):
#         print row
#
# (u'2006-01-05', u'BUY', u'RHAT', 100, 35.14)
# (u'2006-03-28', u'BUY', u'IBM', 1000, 45.0)
# (u'2006-04-06', u'SELL', u'IBM', 500, 53.0)
# (u'2006-04-05', u'BUY', u'MSFT', 1000, 72.0)
