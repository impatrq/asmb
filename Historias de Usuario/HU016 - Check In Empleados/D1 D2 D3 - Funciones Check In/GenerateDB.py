import sqlite3

connection = sqlite3.connect('Cabina.db')
cursor = connection.cursor()


nombres =  [(1,6,"David Mcmillan","09-09-14","lorem.ipsum@Nullam.ca"),(2,10,"Cadman Coffey","02-09-16","tempor.est.ac@fringillaest.edu"),(3,10,"Baker Moreno","17-08-01","per@Nunclectus.com"),(4,11,"Martina Waters","07-06-70","sodales.Mauris.blandit@egetmetusIn.co.uk"),(5,4,"Shannon G. Wright","24-08-62","Cras.vulputate.velit@DonectinciduntDonec.co.uk"),(6,3,"Madaline Jackson","25-01-12","nunc@infelis.ca"),(7,11,"Shelley Livingston","25-07-10","Nullam@aliquetmolestie.net"),(8,6,"Dylan Ingram","24-11-97","tristique.pellentesque.tellus@amet.net"),(9,11,"Valentine I. Prince","29-05-79","Quisque@hymenaeos.co.uk"),(10,6,"Hilary Hampton","28-05-13","aliquet.libero.Integer@Donecnon.ca"),
            (11,3,"Selma V. Anthony","03-04-01","Cras.dolor@nec.com"),(12,14,"Jamal Farmer","29-08-92","ornare@temporarcuVestibulum.edu"),(13,15,"Macaulay Palmer","24-08-79","ipsum@sitamet.co.uk"),(14,12,"Alan K. Britt","13-11-70","velit@etnuncQuisque.org"),(15,10,"Wang N. Cole","14-03-96","tempus.lorem@Sedpharetra.co.uk"),(16,4,"Tatum U. Haney","16-03-89","ridiculus.mus.Proin@egetmetus.co.uk"),(17,5,"Barbara I. Peck","26-11-71","ornare@vitaealiquet.co.uk"),(18,1,"Seth L. Swanson","02-09-64","gravida.sagittis@metusAeneansed.edu"),(19,10,"Jameson Mccall","23-10-19","ligula.Aenean.euismod@etultrices.org"),(20,11,"Quincy Roth","30-07-83","dignissim@egestasascelerisque.org"),
            (21,10,"Patience T. Holmes","26-10-72","orci@nonlacinia.org"),(22,6,"Nolan Vinson","07-05-68","conubia.nostra@risusNullaeget.net"),(23,5,"Eleanor Sanchez","15-06-13","tellus.Aenean@massa.co.uk"),(24,10,"Wade N. Snider","15-07-81","Nullam.ut.nisi@necmauris.co.uk"),(25,12,"Grady J. Nunez","19-10-69","porttitor.tellus@estNunc.com"),(26,5,"Chanda Walter","03-01-78","vitae.diam@odio.edu"),(27,11,"Emery R. Sandoval","05-07-80","penatibus@risus.co.uk"),(28,1,"Melodie C. Mcmahon","11-04-82","mi.ac.mattis@semconsequatnec.co.uk"),(29,1,"Derek E. Lott","01-08-03","augue.ut@a.com"),(30,14,"Hammett Joseph","17-12-75","et.euismod@lacusAliquam.com"),
            (31,15,"Griffin M. Mcgee","14-05-10","lacinia.mattis@urna.edu"),(32,11,"Dillon R. Cannon","19-05-92","erat@apurusDuis.com"),(33,13,"Malik W. Wood","24-06-70","elit@magna.com"),(34,8,"Dale U. Thornton","07-09-75","viverra@magnis.edu"),(35,12,"Haviva Fox","20-11-94","ligula@ascelerisque.net"),(36,13,"Callum J. Blackburn","29-08-05","massa.rutrum@consequat.edu"),(37,11,"Ferdinand V. Knowles","05-04-84","arcu@odioNam.org"),(38,3,"Amos S. Robinson","10-01-95","facilisis.eget@Sed.co.uk"),(39,5,"Hyatt Osborne","15-11-84","mauris.sagittis@Integeraliquamadipiscing.co.uk"),(40,1,"Maia L. Tanner","18-05-22","imperdiet.nec.leo@vulputatemaurissagittis.com"),
            (41,3,"Wade Rich","19-10-98","magna.a@sodalesnisi.org"),(42,12,"Laith Scott","01-10-88","eget@Sed.co.uk"),(43,13,"Shelley P. Warren","07-04-68","vulputate.risus.a@scelerisque.co.uk"),(44,12,"Dominic Melendez","03-09-99","ligula.Aliquam@neque.org"),(45,3,"Adele Russell","13-12-70","mi@nibhlacinia.org"),(46,15,"Kyle Wright","04-11-87","Fusce@loremloremluctus.co.uk"),(47,7,"Vanna Ortiz","28-11-68","condimentum@pellentesquemassalobortis.ca"),(48,13,"Lana Ayers","30-11-73","eros.Proin.ultrices@nunc.edu"),(49,1,"Merritt P. Mccormick","04-11-85","ipsum.dolor.sit@Aliquamgravida.org"),(50,1,"Tatiana Mcgowan","12-02-85","Proin.vel@eratvitaerisus.edu"),
            (51,5,"Quintessa Colon","18-01-61","interdum.ligula@sollicitudin.com"),(52,10,"Simon Jackson","07-11-93","ut.nulla@rhoncusNullam.co.uk"),(53,7,"Merrill Hunt","25-11-83","quam.vel.sapien@sedleo.edu"),(54,6,"Tucker T. Weiss","06-04-91","et@luctus.org"),(55,9,"Kamal Holmes","24-04-94","ultrices@egettincidunt.ca"),(56,7,"Melissa Y. Stephens","30-09-64","erat@egestas.org"),(57,3,"Lilah Moore","08-08-17","risus.Donec.nibh@aliquetodio.org"),(58,6,"Kendall Conway","11-04-73","iaculis.nec@dui.com"),(59,7,"Laith J. Jefferson","25-09-16","penatibus@amet.org"),(60,11,"Maxine X. Baird","29-05-63","in.felis.Nulla@lacusMaurisnon.com"),
            (61,9,"Travis Melendez","25-03-89","auctor.nunc.nulla@velitegestas.org"),(62,15,"Uma Dalton","07-05-92","urna.Nunc@lobortisultrices.edu"),(63,1,"Wallace Brewer","05-07-62","mattis.ornare.lectus@velarcu.net"),(64,1,"Stephanie X. Barnett","07-06-14","tincidunt@erat.edu"),(65,6,"Jaden B. Patel","16-04-13","Sed@Nuncuterat.co.uk"),(66,6,"Britanni Cash","19-12-82","ante.bibendum.ullamcorper@senectus.co.uk"),(67,9,"Ivy U. Trevino","18-09-02","et.rutrum@scelerisque.net"),(68,3,"Leah V. Dunlap","14-05-75","eu.metus.In@molestie.edu"),(69,4,"Zane V. Dawson","10-11-61","nulla@elit.co.uk"),(70,11,"Farrah S. Johnston","15-02-13","dis.parturient@elitAliquamauctor.edu"),
            (71,2,"Aladdin L. Maddox","27-02-92","eu.tellus.eu@dolor.org"),(72,14,"Plato Watts","15-06-17","Nunc.quis@lorem.org"),(73,12,"Renee G. Allen","08-08-81","Morbi.non.sapien@dolortempusnon.edu"),(74,12,"Yvette Waters","19-02-08","pede.blandit@arcuMorbisit.edu"),(75,4,"Leonard N. Harding","01-04-95","quis.turpis.vitae@inconsectetuer.org"),(76,10,"Dustin J. Burns","20-04-98","leo.elementum.sem@Sed.org"),(77,10,"Ella Holmes","07-07-01","ut@non.org"),(78,4,"Elmo B. Kirby","06-11-71","nibh@vel.co.uk"),(79,4,"Cedric Q. Shaffer","22-03-78","ante.iaculis.nec@cursus.net"),(80,8,"Scarlett Cortez","06-12-78","nunc.interdum@ut.net"),
            (81,7,"Geraldine N. Odonnell","01-04-84","Nulla.eget.metus@habitantmorbitristique.net"),(82,4,"Yoshio S. Robbins","27-05-89","eget.metus.eu@pedePraesenteu.net"),(83,12,"Anastasia I. Kirby","06-09-82","Mauris.vel.turpis@augue.edu"),(84,11,"Sylvester Valdez","12-11-74","aliquam@euismodest.edu"),(85,5,"Dominic P. Logan","15-02-69","eu@interdumCurabitur.net"),(86,13,"Declan Mcknight","09-11-69","varius.Nam.porttitor@Sed.edu"),(87,5,"Davis Barr","06-03-17","Aliquam.adipiscing.lobortis@pellentesqueegetdictum.ca"),(88,2,"Roary E. Ortega","14-02-16","nascetur@ut.com"),(89,2,"Lamar F. Harding","18-11-00","pulvinar@Phasellusdapibusquam.com"),(90,7,"Deanna L. Collier","28-04-85","convallis.erat@libero.net"),
            (91,13,"Neville J. Massey","23-02-72","elit.pharetra@fermentumfermentum.net"),(92,10,"Kiara Mack","19-10-16","nisl.Maecenas.malesuada@laoreetlectus.edu"),(93,1,"Quemby M. Floyd","12-01-74","dictum@In.org"),(94,4,"Aubrey Stark","25-05-68","vitae.aliquet@ametrisusDonec.com"),(95,9,"Hakeem Lowery","23-02-96","sed.orci.lobortis@cursuspurus.ca"),(96,7,"Pascale Nolan","08-06-70","arcu@faucibus.ca"),(97,13,"Echo K. Suarez","11-06-13","libero.Donec@fringilla.ca"),(98,14,"Moses I. Cobb","29-03-68","sem@enimnisl.com"),(99,7,"Kelsey D. Mcleod","25-12-90","semper@Vivamus.edu"),(100,6,"Cedric Kim","19-08-68","vitae.posuere.at@Quisqueimperdiet.edu")]

horarios = [(('08:15:00-16:30:00'),('08:15:00-16:30:00'),('08:15:00-16:30:00'),('08:15:00-16:30:00'),('08:15:00-16:30:00'),('08:15:00-16:30:00'),('08:15:00-16:30:00')),
            (('09:50:00-19:50:00'),('09:50:00-19:50:00'),('09:50:00-19:50:00'),('09:50:00-19:50:00'),('09:50:00-19:50:00'),('09:50:00-19:50:00'),('09:50:00-19:50:00')),
            (('10:10:00-19:05:00'),('10:10:00-19:05:00'),('10:10:00-19:05:00'),('10:10:00-19:05:00'),('10:10:00-19:05:00'),('10:10:00-19:05:00'),('10:10:00-19:05:00')),
            (('23:50:00-05:30:00'),('23:50:00-05:30:00'),('23:50:00-05:30:00'),('23:50:00-05:30:00'),('23:50:00-05:30:00'),('23:50:00-05:30:00'),('23:50:00-05:30:00')),
            (('00:00:00-04:50:00'),('00:00:00-04:50:00'),('00:00:00-04:50:00'),('00:00:00-04:50:00'),('00:00:00-04:50:00'),('00:00:00-04:50:00'),('00:00:00-04:50:00')),
            (('08:15:00-16:30:00'),('08:15:00-16:30:00'),('08:15:00-16:30:00'),('08:15:00-16:30:00'),('08:15:00-16:30:00'),('08:15:00-16:30:00'),('08:15:00-16:30:00')),
            (('09:50:00-19:50:00'),('09:50:00-19:50:00'),('09:50:00-19:50:00'),('09:50:00-19:50:00'),('09:50:00-19:50:00'),('09:50:00-19:50:00'),('09:50:00-19:50:00')),
            (('10:10:00-19:05:00'),('10:10:00-19:05:00'),('10:10:00-19:05:00'),('10:10:00-19:05:00'),('10:10:00-19:05:00'),('10:10:00-19:05:00'),('10:10:00-19:05:00')),
            (('23:50:00-05:30:00'),('23:50:00-05:30:00'),('23:50:00-05:30:00'),('23:50:00-05:30:00'),('23:50:00-05:30:00'),('23:50:00-05:30:00'),('23:50:00-05:30:00')),
            (('00:00:00-04:50:00'),('00:00:00-04:50:00'),('00:00:00-04:50:00'),('00:00:00-04:50:00'),('00:00:00-04:50:00'),('00:00:00-04:50:00'),('00:00:00-04:50:00')),
            (('08:15:00-16:30:00'),('08:15:00-16:30:00'),('08:15:00-16:30:00'),('08:15:00-16:30:00'),('08:15:00-16:30:00'),('08:15:00-16:30:00'),('08:15:00-16:30:00')),
            (('09:50:00-19:50:00'),('09:50:00-19:50:00'),('09:50:00-19:50:00'),('09:50:00-19:50:00'),('09:50:00-19:50:00'),('09:50:00-19:50:00'),('09:50:00-19:50:00')),
            (('10:10:00-19:05:00'),('10:10:00-19:05:00'),('10:10:00-19:05:00'),('10:10:00-19:05:00'),('10:10:00-19:05:00'),('10:10:00-19:05:00'),('10:10:00-19:05:00')),
            (('23:50:00-05:30:00'),('23:50:00-05:30:00'),('23:50:00-05:30:00'),('23:50:00-05:30:00'),('23:50:00-05:30:00'),('23:50:00-05:30:00'),('23:50:00-05:30:00')),
            (('00:00:00-04:50:00'),('00:00:00-04:50:00'),('00:00:00-04:50:00'),('00:00:00-04:50:00'),('00:00:00-04:50:00'),('00:00:00-04:50:00'),('00:00:00-04:50:00'))]

cmd = """CREATE TABLE IF NOT EXISTS Empleados(
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        workschedule INTEGER NOT NULL,
        name TEXT NOT NULL,
        birth DATE NOT NULL,
        email TEXT NOT NULL
    )"""
cursor.execute(cmd)

cmd = """CREATE TABLE IF NOT EXISTS Horarios(
        workschedule INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        monday TEXT DEFAULT NULL,
        tuesday TEXT DEFAULT NULL,
        wednesday TEXT DEFAULT NULL,
        thursday TEXT DEFAULT NULL,
        friday TEXT DEFAULT NULL,
        saturday TEXT DEFAULT NULL,
        sunday TEXT DEFAULT NULL
     )"""
cursor.execute(cmd)

cmd = """CREATE TABLE IF NOT EXISTS Entradas(
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        empleadoid INTEGER NOT NULL,
        day DATE NOT NULL,
        checkin TIME NOT NULL,
        pretendedcheckin TIME DEFAULT NULL
    )"""
cursor.execute(cmd)

for id, group, name, birth, email in nombres:
    cmd = f"""INSERT INTO Empleados ('id','workschedule','name','birth','email') VALUES ('{id}','{group}','{name}','{birth}','{email}')"""
    cursor.execute(cmd)
    connection.commit()

for monday, tuesday, wednesday, thursday, friday, saturday, sunday in horarios:
    cmd = f"""INSERT INTO Horarios (monday, tuesday, wednesday, thursday, friday, saturday, sunday) VALUES ('{monday}','{tuesday}','{wednesday}','{thursday}','{friday}','{saturday}','{sunday}')"""
    cursor.execute(cmd)
    connection.commit()


