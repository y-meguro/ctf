e1 = 11
c1 = 80265690974140286785447882525076768851800986505783169077080797677035805215248640465159446426193422263912423067392651719120282968933314718780685629466284745121303594495759721471318134122366715904

e2 = 13
c2 = 14451037575679461333658489727928902053807202350950440400755535465672646289383249206721118279217195146247129636809289035793102103248547070620691905918862697416910065303500798664102685376006097589955370023822867897020714767877873664

n = 236934049743116267137999082243372631809789567482083918717832642810097363305512293474568071369055296264199854438630820352634325357252399203160052660683745421710174826323192475870497319105418435646820494864987787286941817224659073497212768480618387152477878449603008187097148599534206055318807657902493850180695091646575878916531742076951110529004783428260456713315007812112632429296257313525506207087475539303737022587194108436132757979273391594299137176227924904126161234005321583720836733205639052615538054399452669637400105028428545751844036229657412844469034970807562336527158965779903175305550570647732255961850364080642984562893392375273054434538280546913977098212083374336482279710348958536764229803743404325258229707314844255917497531735251105389366176228741806064378293682890877558325834873371615135474627913981994123692172918524625407966731238257519603614744577

# e1*s1 + e2*s2 = 1 となるような s1, s2 を求める
def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extended_gcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    return x % m

def attack(c1, c2, e1, e2, n):
    gcd, s1, s2 = extended_gcd(e1, e2)
    if s1 < 0:
        s1 = -s1
        c1 = modinv(c1, n)
    elif s2 < 0:
        s2 = -s2
        c2 = modinv(c2, n)

    v = pow(c1, s1, n)
    w = pow(c2, s2, n)
    x = (v * w) % n
    return x

print(attack(c1, c2, e1, e2, n))
