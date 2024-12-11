print("Data Types")
print("String")
print("String Formatting")

str1 = "string"
print(str1.center(20))
print(str1.center(20, "-"))

print("my\tfavorite\tgame")
print("my\tfavorite\tgame".expandtabs(tabsize=8))

str1 = "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Rerum iure illo esse hic optio eaque aperiam quis recusandae, distinctio repudiandae, unde officia! Officiis omnis minus accusantium. Placeat quas delectus exercitationem nostrum ipsam ratione quaerat, nihil saepe optio dolorum sint dolores numquam eveniet consequatur at laboriosam obcaecati eum voluptates reiciendis aut ipsa? Voluptates nesciunt aliquid minus amet sunt atque cum pariatur, labore veritatis enim repellendus dolorem corporis obcaecati quibusdam a cupiditate saepe facilis alias? At pariatur temporibus, tenetur veritatis cupiditate debitis dignissimos voluptatibus obcaecati ex dolorum atque laudantium quaerat similique eaque aliquid consequuntur, totam sed in! Eaque odit pariatur fugiat vero?"

str1 = "hello"
print(str1.ljust(50, "*"))

str1 = "   one   two   three   "
print(str1)
print(str1.lstrip())

str1 = "***one\ttwo\tthree"
print(str1)
print(str1.lstrip("*"))

str1 = "Today is a different day and it's not like yesterday"
print(str1)
print(str1.replace("day", "night"))

str2 = str1.replace("day", "night")
print(str2)

str2 = str1.replace("day", "night", 2)
print(str2)

str1 = "one\ttwo\tthree***"
print(str1)
print(str1.rstrip("*"))

str1 = "hello"
print(str1.rjust(70))
print(str1.rjust(70, "*"))

str1 = "\tone\ttwo\tthree\t"
print(str1)
print(str1.rstrip())

str1 = "hello,*****"
print(str1.rstrip(",*"))

str1 = "    hello   "
print(str1,"_")
print(str1.strip(),"_")
print(str1.zfill(20))

str2 = "www.realpython.com"
print(str2.strip("w.moc"))
