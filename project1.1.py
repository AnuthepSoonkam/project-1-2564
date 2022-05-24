import sqlite3
import os

conn = sqlite3.connect(r'D:\pthones\project1.1.db')
c = conn.cursor()
x = []
y = []
xy = []
yx = []
clog1 = []
clog2 = ["รองเท้าหัวโต แบบเสริมส้น สีขาว",'รองเท้าหัวโต แบบเสริมส้น สีชมพู','รองเท้าหัวโต แบบธรรมดา สีขาว','รองเท้าหัวโต แบบเสริมส้น สีฟ้าเขียว','รองเท้าหัวโต แบบเสริมส้น สีชมพูส้ม']
clog3 = ["รองเท้าหัวโต แบบเสริมส้น สีขาว   ",'รองเท้าหัวโต แบบเสริมส้น สีชมพู   ','รองเท้าหัวโต แบบธรรมดา สีขาว   ','รองเท้าหัวโต แบบเสริมส้น สีฟ้าเขียว','รองเท้าหัวโต แบบเสริมส้น สีชมพูส้ม ']

def create_shop(): 
        user = """CREATE TABLE "user"( 
        "queue" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        "first_name" TEXT NOT NULL,
        "last_name" TEXT NOT NULL
        )"""
        
        contact = """CREATE TABLE "contact"(
        "queue" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        "phone_number" TEXT NOT NULL,
        "gmail" TEXT NOT NULL,
        "facebook" TEXT NOT NULL
        )"""

        clogs = """CREATE TABLE "clogs"(
        "queue" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        "size" TEXT NOT NULL,
        "type" TEXT NOT NULL,
        "props" TEXT NOT NULL
        )"""
        
        address = """CREATE TABLE "address"(
        "queue" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        "house_number" TEXT NOT NULL,
        "village_number" TEXT NOT NULL,
        "village_name" TEXT NOT NULL,        
        "soi" TEXT NOT NULL,
        "road_name" TEXT NOT NULL,
        "sub_district" TEXT NOT NULL,
        "district" TEXT NOT NULL,
        "province" TEXT NOT NULL,
        "postal_code" TEXT NOT NULL
        )"""

        conn.execute(user)
        conn.execute(contact)
        conn.execute(clogs)
        conn.execute(address)

def menu(): 
    os.system ('cls')
    print('\U0001F461 โปรแกรมจัดการข้อมูลเกี่ยวกับการค้าขายสินค้าหลักหลังบ้าน ร้าน รองเท้าหัวโต \U0001F435\n   ลงชื่อเข้าใช้และเลือกสินค้า กด 1\n   แก้ไขรายการ           กด 2\n   แสดงรายการ           กด 3\n   ออกจากโปรแกรม        กด 4\n')
    a = input('   โปรดเลือกตัวเลือก: ')

    if a == '1':
        login_and_select()
        torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
        menu()

    elif a == '2': 
        edit()
        torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
        menu()
    
    elif a == '3':
        for i in conn.execute("""SELECT * FROM clogs"""):
            clog1.extend(i)
        for i in range(len(clog2)):
            print(clog3[i] ,"= ",clog1.count(clog2[i]))
        show()
        torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
        menu()

    elif a == '4':
        exitto()
        menu()

    else:
        print('ERROR กลับไปเริ่มใหม่')
        menu()

def login_and_select():
    os.system ('cls') 

    sql1 = """INSERT INTO 'user' (first_name,last_name)
        VALUES (?,?)"""
    x.clear()
    A = input('ชื่อจริง           : ')
    if A != '':
        for a in A:
            z = a.isnumeric()
            if z == True:
                print('\nโปรดใส่ข้อมูลให้ถูกต้อง')
                x.clear()
                torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
                menu()
        x.append(A)
    else:
        print('\nโปรดใส่ข้อมูล')
        x.clear()
        torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
        menu()

    B = input('\nนามสกุล          :    ')
    if B != '':
        for a in B:
            z = a.isnumeric()
            if z == True:
                print('\nโปรดใส่ข้อมูลให้ถูกต้อง')
                x.clear()
                torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
                menu()
        x.append(B)
    else:
        print('\nโปรดใส่ข้อมูล')
        x.clear()
        torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
        menu()

    c.execute(sql1,x)

    os.system ('cls')

    sql2 = """INSERT INTO 'contact' (phone_number,gmail,facebook)
        VALUES (?,?,?)"""
    y.clear()
    C = input('\nเบอร์โทรศัพท์   :    ')
    if C != '':
        for a in C:
            z = a.isnumeric()
            if z == False:
                print('\nโปรดใส่ข้อมูลให้ถูกต้อง')
                y.clear()
                torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
                menu()
        y.append(C)
    else:
        print('\nโปรดใส่ข้อมูล')
        y.clear()
        torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
        menu()

    D = input('\nGmail   :    ')
    if D != '':
        y.append(D)
    else:
        print('\nโปรดใส่ข้อมูล')
        y.clear()
        torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
        menu()

    E = input('\nFacebook   :    ')
    if E != '':
        y.append(E)
    else:
        print('\nโปรดใส่ข้อมูล')
        y.clear()
        torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
        menu()

    c.execute(sql2,y)

    os.system ('cls')
    xy.clear()
    sql3 = """INSERT INTO 'clogs' (size,type,props)
        VALUES (?,?,?)"""
    print('ไซส์ รองเท้า')
    F = input('\nไซส์  :  ')
    if F != '':
        for a in F:
            z = a.isnumeric()
            if z == False:
                print('\nโปรดใส่ข้อมูลให้ถูกต้อง')
                xy.clear()
                torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
                menu()
        xy.append(F)
    else:
        print('\nโปรดใส่ข้อมูล')
        xy.clear()
        torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
        menu()

    os.system ('cls')    
    print('1. รองเท้าหัวโต แบบเสริมส้น สีขาว    \U0001F90D\U0001F90D 220 บาท\n2. รองเท้าหัวโต แบบเสริมส้น สีชมพู    \U0001F43D\U0001F43D 220 บาท\n3. รองเท้าหัวโต แบบธรรมดา สีขาว    \U0001F90D\U0001F90D 169 บาท\n4. รองเท้าหัวโต แบบเสริมส้น สีฟ้าเขียว \U0001F499\U0001F49A 220 บาท\n5. รองเท้าหัวโต แบบเสริมส้น สีชมพูส้ม  \U0001F43D\U0001F9E1 220 บาท')
    
    G = input('\nแบบรองเท้า  :  ')
    if G != '':
        for a in G:
            z = a.isnumeric()
            if z == False:
                print('\nโปรดใส่ข้อมูลให้ถูกต้อง')
                xy.clear()
                torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
                menu()
        if G == '1':
            xy.append('รองเท้าหัวโต แบบเสริมส้น สีขาว')
        if G == '2':
            xy.append('รองเท้าหัวโต แบบเสริมส้น สีชมพู')
        if G == '3':
            xy.append('รองเท้าหัวโต แบบธรรมดา สีขาว')
        if G == '4':
            xy.append('รองเท้าหัวโต แบบเสริมส้น สีฟ้าเขียว')
        if G == '5':
            xy.append('รองเท้าหัวโต แบบเสริมส้น สีชมพูส้ม')

    else:
        print('\nโปรดใส่ข้อมูล')
        xy.clear()
        torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
        menu()

    os.system ('cls')   
    print('JIBBITZ ทั้ง 23 แบบ \U0001F435\n ')
    H = input('\nJIBBITZ ถ้าอยากได้หลายแบบให้ใส่เลขแบบแล้วคั่นด้วย "," *ตัวอย่าง : 1,2,3\n        ถ้าไม่ค้องการให้ใส่ "-" \n\nJIBBITZ ที่เเลือก : ')   
    if H != '':
        xy.append(H)
    else:
        print('\nโปรดใส่ข้อมูล')
        xy.clear()
        torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
        menu()

    c.execute(sql3,xy)

    os.system ('cls') 
    yx.clear()
    sql4 = """INSERT INTO 'address' (house_number,village_number,village_name,soi,road_name,sub_district,district,province,postal_code)
        VALUES (?,?,?,?,?,?,?,?,?)"""
    I = input('บ้านเลขที่ : ')
    if I != '':
        yx.append(I)
    else:
        print('\nโปรดใส่ข้อมูล')
        yx.clear()
        torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
        menu()

    J = input('หมู่ : ')
    if J != '':
        for a in J:
            z = a.isnumeric()
            if z == False:
                print('\nโปรดใส่ข้อมูลให้ถูกต้อง')
                xy.clear()
                torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
                menu()
        yx.append(J)
    else:
        print('\nโปรดใส่ข้อมูล')
        yx.clear()
        torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
        menu()

    K = input('ชื่อหมู่บ้าน : ')
    if K != '':
        yx.append(K)
    else:
        print('\nโปรดใส่ข้อมูล')
        yx.clear()
        torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
        menu()

    L = input('ถนน : ')
    if L != '':
        yx.append(L)
    else:
        print('\nโปรดใส่ข้อมูล')
        yx.clear()
        torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
        menu()

    M = input('ซอย : ')
    if M != '':
        yx.append(M)
    else:
        print('\nโปรดใส่ข้อมูล')
        yx.clear()
        torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
        menu()

    N = input('ตำบล : ')
    if N != '':
        for a in N:
            z = a.isnumeric()
            if z == True:
                print('\nโปรดใส่ข้อมูลให้ถูกต้อง')
                xy.clear()
                torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
                menu()
        yx.append(N)
    else:
        print('\nโปรดใส่ข้อมูล')
        yx.clear()
        torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
        menu()

    O = input('อำเภอ : ')
    if O != '':
        for a in O:
            z = a.isnumeric()
            if z == True:
                print('\nโปรดใส่ข้อมูลให้ถูกต้อง')
                xy.clear()
                torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
                menu()
        yx.append(O)
    else:
        print('\nโปรดใส่ข้อมูล')
        yx.clear()
        torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
        menu()

    P = input('จังหวัด : ')
    if P != '':
        for a in P:
            z = a.isnumeric()
            if z == True:
                print('\nโปรดใส่ข้อมูลให้ถูกต้อง')
                xy.clear()
                torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
                menu()
        yx.append(P)
    else:
        print('\nโปรดใส่ข้อมูล')
        yx.clear()
        torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
        menu()

    Q = input('รหัสไปรษณีย์ : ')
    if Q != '':
        for a in Q:
            z = a.isnumeric()
            if z == False:
                print('\nโปรดใส่ข้อมูลให้ถูกต้อง')
                xy.clear()
                torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
                menu()
        yx.append(Q)
    else:
        print('\nโปรดใส่ข้อมูล')
        yx.clear()
        torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
        menu()

    c.execute(sql4,yx)
    conn.commit()
    print('\nทำรายการเสร็จสิ้น')

def edit(): 
    os.system ('cls')
    the_way = input('เลือกรายการที่ต้องการแก้ไข\nชื่อ-นามสกุล      กด 1\nช่องทางการติดต่อ  กด 2\nรองเท้าหัวโต     กด 3\nที่อยู่            กด 4\n\n รายการที่ต้องการจะแก้ไข : ')
    if the_way == '1':
        print('ลำดับ / ชื่อจริง / นามสกุล \n')
        name = """SELECT * FROM user"""
        for x in c.execute(name):
            print('-'*65)
            print('  ',x[0],' /',x[1],'/',x[2])
        the_edit_way = input('เลือกรายการที่จะแก้ไข\nชื่อจริง             กด 1\nนามสกุล            กด 2\n\n รายการที่ต้องการจะแก้ไข : ')
        if the_edit_way == '1':
            sql = """UPDATE user SET first_name = ? WHERE queue = ?"""
            A = input('ชื่อจริง    ที่ต้องการให้เป็น : ')
            if A != '':
                for a in A:
                    z = a.isnumeric()
                    if z == True:
                        print('\nโปรดใส่ข้อมูลให้ถูกต้อง')
                        torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
                        menu()
            else:
                print('\nโปรดใส่ข้อมูล')
                torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
                menu()
            B = input('\nลำดับ     ที่ต้องการเปลี่ยน : ')
            if B != '':
                for a in B:
                    z = a.isnumeric()
                    if z == False:
                        print('\nโปรดใส่ข้อมูลให้ถูกต้อง')
                        torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
                        menu()
            else:
                print('\nโปรดใส่ข้อมูล')
                torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
                menu()
            zy = (A,B)
            c.execute(sql,zy)
            conn.commit()
            print('\nทำรายการเสร็จสิ้น')

        if the_edit_way == '2':
            sql = """UPDATE user SET last_name = ? WHERE queue = ?"""
            A = input('นามสกุล     ที่ต้องการให้เป็น : ')
            if A != '':
                for a in A:
                    z = a.isnumeric()
                    if z == True:
                        print('\nโปรดใส่ข้อมูลให้ถูกต้อง')
                        torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
                        menu()
            else:
                print('\nโปรดใส่ข้อมูล')
                torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
                menu()
            B = input('\nลำดับ       ที่ต้องการเปลี่ยน : ')
            if B != '':
                for a in B:
                    z = a.isnumeric()
                    if z == False:
                        print('\nโปรดใส่ข้อมูลให้ถูกต้อง')
                        torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
                        menu()
            else:
                print('\nโปรดใส่ข้อมูล')
                torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
                menu()
            zy = (A,B)
            c.execute(sql,zy)
            conn.commit()
            print('\nทำรายการเสร็จสิ้น')
        else:
            print('ERROR กลับไปเริ่มใหม่')
            menu()

    if the_way == '2':
        print('ลำดับ / หมายเลขโทรศัพท์ / Gmail / Facebook \n')
        name = """SELECT * FROM contact"""
        for x in c.execute(name):
            print('-'*65)
            print('  ',x[0],' /',x[1],'/',x[2],'/',x[3])
        the_edit_way = input('เลือกรายการที่จะแก้ไข\nหมายเลขโทรศัพท์    กด 1\nGmail            กด 2\nFacebook         กด 3\n\n รายการที่ต้องการจะแก้ไข : ')
        if the_edit_way == '1':
            sql = """UPDATE contact SET phone_number = ? WHERE queue = ?"""
            A = input('หมายเลขโทรศัพท์     ที่ต้องการให้เป็น : ')
            if A != '':
                for a in A:
                    z = a.isnumeric()
                    if z == False:
                        print('\nโปรดใส่ข้อมูลให้ถูกต้อง')
                        torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
                        menu()
            else:
                print('\nโปรดใส่ข้อมูล')
                torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
                menu()
            B = input('\nลำดับ               ที่ต้องการเปลี่ยน : ')
            if B != '':
                for a in B:
                    z = a.isnumeric()
                    if z == False:
                        print('\nโปรดใส่ข้อมูลให้ถูกต้อง')
                        torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
                        menu()
            else:
                print('\nโปรดใส่ข้อมูล')
                torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
                menu()
            zy = (A,B)
            c.execute(sql,zy)
            conn.commit()
            print('\nทำรายการเสร็จสิ้น')

        if the_edit_way == '2':
            sql = """UPDATE contact SET gmail = ? WHERE queue = ?"""
            A = input('Gmail     ที่ต้องการให้เป็น : ')
            if A == '':
                print('\nโปรดใส่ข้อมูล')
                torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
                menu()
            B = input('\nลำดับ      ที่ต้องการเปลี่ยน : ')
            if B != '':
                for a in B:
                    z = a.isnumeric()
                    if z == False:
                        print('\nโปรดใส่ข้อมูลให้ถูกต้อง')
                        torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
                        menu()
            else:
                print('\nโปรดใส่ข้อมูล')
                torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
                menu()
            zy = (A,B)
            c.execute(sql,zy)
            conn.commit()
            print('\nทำรายการเสร็จสิ้น')

        if the_edit_way == '3':
            sql = """UPDATE contact SET facebook = ? WHERE queue = ?"""
            A = input('Facebook     ที่ต้องการให้เป็น : ')
            if A == '':
                print('\nโปรดใส่ข้อมูล')
                torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
                menu()
            B = input('\nลำดับ         ที่ต้องการเปลี่ยน : ')
            if B != '':
                for a in B:
                    z = a.isnumeric()
                    if z == False:
                        print('\nโปรดใส่ข้อมูลให้ถูกต้อง')
                        torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
                        menu()
            else:
                print('\nโปรดใส่ข้อมูล')
                torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
                menu()
            zy = (A,B)
            c.execute(sql,zy)
            conn.commit()
            print('\nทำรายการเสร็จสิ้น')
        else:
            print('ERROR กลับไปเริ่มใหม่')
            menu()

    if the_way == '3':
        print('ลำดับ / ขนาดรองเท้า / แบบรองเท้า / ของตกแต่ง \n')
        name = """SELECT * FROM clogs"""
        for x in c.execute(name):
            print('-'*65)
            print('  ',x[0],' /',x[1],'/',x[2],'/',x[3])
        the_edit_way = input('เลือกรายการที่จะแก้ไข\nไซส์รองเท้า          กด 1\nแบบรองเท้า          กด 2\nJIBBITZ            กด 3\n\n รายการที่ต้องการจะแก้ไข : ')
        if the_edit_way == '1':
            sql = """UPDATE clogs SET size = ? WHERE queue = ?"""
            A = input('ไซส์รองเท้า    ที่ต้องการให้เป็น : ')
            if A != '':
                for a in A:
                    z = a.isnumeric()
                    if z == False:
                        print('\nโปรดใส่ข้อมูลให้ถูกต้อง')
                        torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
                        menu()
            else:
                print('\nโปรดใส่ข้อมูล')
                torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
                menu()
            B = input('\nลำดับ         ที่ต้องการเปลี่ยน : ')
            if B != '':
                for a in B:
                    z = a.isnumeric()
                    if z == False:
                        print('\nโปรดใส่ข้อมูลให้ถูกต้อง')
                        torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
                        menu()
            else:
                print('\nโปรดใส่ข้อมูล')
                torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
                menu()
            zy = (A,B)
            c.execute(sql,zy)
            conn.commit()
            print('\nทำรายการเสร็จสิ้น')

        if the_edit_way == '2':
            sql = """UPDATE clogs SET type = ? WHERE queue = ?"""
            A1 = input('แบบรองเท้า    ที่ต้องการให้เป็น : ')
            if A1 != '':
                for a in A1:
                    z = a.isnumeric()
                    if z == False:
                        print('\nโปรดใส่ข้อมูลให้ถูกต้อง')
                        torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
                        menu()
                if A1 == '1':
                    A ='รองเท้าหัวโต แบบเสริมส้น สีขาว'
                if A1 == '2':
                    A = 'รองเท้าหัวโต แบบเสริมส้น สีชมพู'
                if A1 == '3':
                    A = 'รองเท้าหัวโต แบบธรรมดา สีขาว'
                if A1 == '4':
                    A = 'รองเท้าหัวโต แบบเสริมส้น สีฟ้าเขียว'
                if A1 == '5':
                    A = 'รองเท้าหัวโต แบบเสริมส้น สีชมพูส้ม'
            else:
                print('\nโปรดใส่ข้อมูล')
                torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
                menu()
            B = input('\nลำดับ          ที่ต้องการเปลี่ยน : ')
            if B != '':
                for a in B:
                    z = a.isnumeric()
                    if z == False:
                        print('\nโปรดใส่ข้อมูลให้ถูกต้อง')
                        torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
                        menu()
            else:
                print('\nโปรดใส่ข้อมูล')
                torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
                menu()
            zy = (A,B)
            c.execute(sql,zy)
            conn.commit()
            print('\nทำรายการเสร็จสิ้น')

        if the_edit_way == '3':
            sql = """UPDATE clogs SET props = ? WHERE queue = ?"""
            print('JIBBITZ ทั้ง 23 แบบ \U0001F435\n ')
            A = input('\nJIBBITZ ถ้าอยากได้หลายแบบให้ใส่เลขแบบแล้วคั่นด้วย "," *ตัวอย่าง : 1,2,3\n        ถ้าไม่ค้องการให้ใส่ "-" \n\nJIBBITZ     ที่ต้องการให้เป็น : ')
            if A == '':
                print('\nโปรดใส่ข้อมูล')
                torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
                menu()
            B = input('\nลำดับ         ที่ต้องการเปลี่ยน : ')
            if B != '':
                for a in B:
                    z = a.isnumeric()
                    if z == False:
                        print('\nโปรดใส่ข้อมูลให้ถูกต้อง')
                        torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
                        menu()
            else:
                print('\nโปรดใส่ข้อมูล')
                torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
                menu()
            zy = (A,B)
            c.execute(sql,zy)
            conn.commit()
            print('\nทำรายการเสร็จสิ้น')
        else:
            print('ERROR กลับไปเริ่มใหม่')
            menu()

    if the_way == '4':
        print('ลำดับ / เลขที่บ้าน / หมู่ / บ้าน / ซอย / ถนน / ตำบล / อำเภอ / จังหวัด / รหัสไปรษณีย์\n')
        name = """SELECT * FROM address"""
        for x in c.execute(name):
            print('-'*65)
            print('  ',x[0],' /',x[1],'/',x[2],'/',x[3],'/',x[4],'/',x[5],'/',x[6],'/',x[7],'/',x[8],'/',x[9],'\n')
        the_edit_way = input('เลือกรายการที่จะแก้ไข\nเลขที่บ้าน       กด 1\nหมู่            กด 2\nชื่อหมู่บ้าน       กด 3\nชื่อซอย         กด 4\nชื่อถนน         กด 5\nชื่อตำบล        กด 6\nชื่ออำเภอ       กด 7\nชื่อจังหวัด       กด 8\nเลขรหัสไปรษณีย์  กด 9\n\n รายการที่ต้องการจะแก้ไข : ')
        if the_edit_way == '1':
            sql = """UPDATE address SET house_number = ? WHERE queue = ?"""
            A = input('เลขที่บ้าน     ที่ต้องการให้เป็น : ')
            if A == '':
                print('\nโปรดใส่ข้อมูล')
                torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
                menu()
            B = input('\nลำดับ        ที่ต้องการเปลี่ยน : ')
            if B != '':
                for a in B:
                    z = a.isnumeric()
                    if z == False:
                        print('\nโปรดใส่ข้อมูลให้ถูกต้อง')
                        torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
                        menu()
            else:
                print('\nโปรดใส่ข้อมูล')
                torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
                menu()
            zy = (A,B)
            c.execute(sql,zy)
            conn.commit()
            print('\nทำรายการเสร็จสิ้น')

        if the_edit_way == '2':
            sql = """UPDATE address SET village_number = ? WHERE queue = ?"""
            A = input('หมู่           ที่ต้องการให้เป็น : ')
            if A == '':
                print('\nโปรดใส่ข้อมูล')
                torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
                menu()
            B = input('\nลำดับ         ที่ต้องการเปลี่ยน : ')
            if B != '':
                for a in B:
                    z = a.isnumeric()
                    if z == False:
                        print('\nโปรดใส่ข้อมูลให้ถูกต้อง')
                        torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
                        menu()
            else:
                print('\nโปรดใส่ข้อมูล')
                torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
                menu()
            zy = (A,B)
            c.execute(sql,zy)
            conn.commit()
            print('\nทำรายการเสร็จสิ้น')

        if the_edit_way == '3':
            sql = """UPDATE address SET village_name = ? WHERE queue = ?"""
            A = input('ชื่อหมู่บ้าน     ที่ต้องการให้เป็น : ')
            if A == '':
                print('\nโปรดใส่ข้อมูล')
                torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
                menu()
            B = input('\nลำดับ         ที่ต้องการเปลี่ยน : ')
            if B != '':
                for a in B:
                    z = a.isnumeric()
                    if z == False:
                        print('\nโปรดใส่ข้อมูลให้ถูกต้อง')
                        torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
                        menu()
            else:
                print('\nโปรดใส่ข้อมูล')
                torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
                menu()
            zy = (A,B)
            c.execute(sql,zy)
            conn.commit()
            print('\nทำรายการเสร็จสิ้น')

        if the_edit_way == '4':
            sql = """UPDATE address SET soi = ? WHERE queue = ?"""
            A = input('ชื่อซอย     ที่ต้องการให้เป็น : ')
            if A == '':
                print('\nโปรดใส่ข้อมูล')
                torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
                menu()
            B = input('\nลำดับ       ที่ต้องการเปลี่ยน : ')
            if B != '':
                for a in B:
                    z = a.isnumeric()
                    if z == False:
                        print('\nโปรดใส่ข้อมูลให้ถูกต้อง')
                        torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
                        menu()
            else:
                print('\nโปรดใส่ข้อมูล')
                torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
                menu()
            zy = (A,B)
            c.execute(sql,zy)
            conn.commit()
            print('\nทำรายการเสร็จสิ้น')

        if the_edit_way == '5':
            sql = """UPDATE address SET road_name = ? WHERE queue = ?"""
            A = input('ชื่อถนน     ที่ต้องการให้เป็น : ')
            if A == '':
                print('\nโปรดใส่ข้อมูล')
                torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
                menu()
            B = input('\nลำดับ      ที่ต้องการเปลี่ยน : ')
            if B != '':
                for a in B:
                    z = a.isnumeric()
                    if z == False:
                        print('\nโปรดใส่ข้อมูลให้ถูกต้อง')
                        torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
                        menu()
            else:
                print('\nโปรดใส่ข้อมูล')
                torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
                menu()
            zy = (A,B)
            c.execute(sql,zy)
            conn.commit()
            print('\nทำรายการเสร็จสิ้น')

        if the_edit_way == '6':
            sql = """UPDATE address SET sub_district = ? WHERE queue = ?"""
            A = input('ชื่อตำบล     ที่ต้องการให้เป็น : ')
            if A == '':
                print('\nโปรดใส่ข้อมูล')
                torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
                menu()
            B = input('\nลำดับ       ที่ต้องการเปลี่ยน : ')
            if B != '':
                for a in B:
                    z = a.isnumeric()
                    if z == False:
                        print('\nโปรดใส่ข้อมูลให้ถูกต้อง')
                        torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
                        menu()
            else:
                print('\nโปรดใส่ข้อมูล')
                torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
                menu()
            zy = (A,B)
            c.execute(sql,zy)
            conn.commit()
            print('\nทำรายการเสร็จสิ้น')

        if the_edit_way == '7':
            sql = """UPDATE address SET district = ? WHERE queue = ?"""
            A = input('ชื่ออำเภอ     ที่ต้องการให้เป็น : ')
            if A == '':
                print('\nโปรดใส่ข้อมูล')
                torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
                menu()
            B = input('\nลำดับ        ที่ต้องการเปลี่ยน : ')
            if B != '':
                for a in B:
                    z = a.isnumeric()
                    if z == False:
                        print('\nโปรดใส่ข้อมูลให้ถูกต้อง')
                        torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
                        menu()
            else:
                print('\nโปรดใส่ข้อมูล')
                torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
                menu()
            zy = (A,B)
            c.execute(sql,zy)
            conn.commit()
            print('\nทำรายการเสร็จสิ้น')

        if the_edit_way == '8':
            sql = """UPDATE address SET province = ? WHERE queue = ?"""
            A = input('ชื่อจังหวัด     ที่ต้องการให้เป็น : ')
            if A == '':
                print('\nโปรดใส่ข้อมูล')
                torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
                menu()
            B = input('\nลำดับ        ที่ต้องการเปลี่ยน : ')
            if B != '':
                for a in B:
                    z = a.isnumeric()
                    if z == False:
                        print('\nโปรดใส่ข้อมูลให้ถูกต้อง')
                        torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
                        menu()
            else:
                print('\nโปรดใส่ข้อมูล')
                torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
                menu()
            zy = (A,B)
            c.execute(sql,zy)
            conn.commit()
            print('\nทำรายการเสร็จสิ้น')

        if the_edit_way == '9':
            sql = """UPDATE address SET postal_code = ? WHERE queue = ?"""
            A = input('รหัสไปรษณีย์     ที่ต้องการให้เป็น : ')
            if A == '':
                print('\nโปรดใส่ข้อมูล')
                torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
                menu()
            B = input('\nลำดับ           ที่ต้องการเปลี่ยน : ')
            if B != '':
                for a in B:
                    z = a.isnumeric()
                    if z == False:
                        print('\nโปรดใส่ข้อมูลให้ถูกต้อง')
                        torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
                        menu()
            else:
                print('\nโปรดใส่ข้อมูล')
                torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
                menu()
            zy = (A,B)
            c.execute(sql,zy)
            conn.commit()
            print('\nทำรายการเสร็จสิ้น')

        else:
            print('ERROR กลับไปเริ่มใหม่')
            menu()

    else:
        print('ERROR กลับไปเริ่มใหม่')
        menu()

def show():
    theway = input('\n\nเลือกรายการที่ต้องการ\n\nกด 1 เพื่อแสดงรายชื่อ\nกด 2 เพื่อแสดงช่องทางการติดต่อ\nกด 3 เพื่อแสดงรายละเอียดรองเท้า\nกด 4 เพื่อแสดงที่อยู่\nกด 5 เพื่อออกไปยังหน้าหลัก\n')
    if theway == '1':
        print('ลำดับ / ชื่อจริง / นามสกุล \n')
        name = """SELECT * FROM user"""
        for x in c.execute(name):
            print('-'*65)
            print('  ',x[0],' /',x[1],'/',x[2])

    if theway == '2':
        print('ลำดับ / หมายเลขโทรศัพท์ / Gmail / Facebook \n')
        name = """SELECT * FROM contact"""
        for x in c.execute(name):
            print('-'*65)
            print('  ',x[0],' /',x[1],'/',x[2],'/',x[3])

    if theway == '3':
        print('ลำดับ / ขนาดรองเท้า / แบบรองเท้า / ของตกแต่ง \n')
        name = """SELECT * FROM clogs"""
        for x in c.execute(name):
            print('-'*65)
            print('  ',x[0],' /',x[1],'/',x[2],'/',x[3])

    if theway == '4':
        print('ลำดับ / เลขที่บ้าน / หมู่ / บ้าน / ซอย / ถนน / ตำบล / อำเภอ / จังหวัด / รหัสไปรษณีย์\n')
        name = """SELECT * FROM address"""
        for x in c.execute(name):
            print('-'*65)
            print('  ',x[0],' /',x[1],'/',x[2],'/',x[3],'/',x[4],'/',x[5],'/',x[6],'/',x[7],'/',x[8],'/',x[9])

    if theway == '5':
        menu()



def exitto():
    os.system ('cls')
    back = str(input('ต้องการออกจากโปรแกรมใช่หรือไม่ y/n : '))
    if back == 'n':
        print('\nWELCOME BACK \U0001F603\n')
        torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')

    elif back == 'y':
        print('\nทำรายการเสร็จสิ้น')
        print('\nBYE-BYE \U0001F44B\n')
        exit()
    else:
        print('\nERROR กลับไปเริ่มใหม่')
        torestart = input('\nกด enter เพื่อกลับไปยัง menu.\n')
        menu() 

# create_shop()
menu()