with open('attending.txt') as file:
    attending = set( line.strip().lower() for line in file )

with open('all.txt', 'r') as file:
    with open('absentees.txt', 'w') as out:
        for line in file:
            line = line.strip().lower()
            if line not in attending:
                out.write(f'{line}\n')