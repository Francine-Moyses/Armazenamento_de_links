for lista in lista:
    cursor.execute("""
        INSERT INTO lista(titulo, link)
        VALUES (?, ?)
    """,(lista['titulo'],lista['link']))

conn.commit()
conn.close()
