def main():

    cats = [
        {"name": "ocicat", "char": "hairy", "mood": "angry"},
        {"name": "selkirk", "char": "hairy", "mood": "calm"},
        {"name": "Rex", "char": "skinny", "mood": "abnoxious"},
        {"name": "Sphynx", "char": "skinny", "mood": "angry"},
        {"name": "Minskin", "char": "black", "mood": "scared"},
        ]

    for cat in cats:
        print(cat["name"], cat["char"], cat["mood"], sep=", ")

main()

'''
1. Ocicat
2. Selkirk Rex
3. Sphynx
4. Minskin 
5. Singapura 
6. Napoleon
7. Peterbald
8. LaPerm
9. Khao Mane
10. Lykoi 
'''