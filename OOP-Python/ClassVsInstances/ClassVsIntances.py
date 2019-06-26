class Hero:
    def __init__(self, para_ten, para_vu_khi, para_mau_sac):
        self.ten = "Sieu nhan " +para_ten
        self.vu_khi = para_vu_khi
        self.mau_sac = para_mau_sac

    def xin_chao(self):
        return "Xin chao, ta chinh la " + self.ten
    # pass

hero_A= Hero("Kteam","Kien thuc","Tim")   # hero_A chính là 1 object thuộc lớp Hero.

# hero_A.ten = "Sieu nhan Do"
# hero_A.vu_khi = "kiem"
# hero_A.mau_sac = "Do"

print(hero_A)  # in ra đối tượng Hero ở hàm Main
print("ten la: ", hero_A.ten)
print("mau sac la: ", hero_A.mau_sac)
print("vu khi la: ", hero_A.vu_khi)
print(hero_A.xin_chao())
print(Hero.xin_chao(hero_A))
# print(hero_A.aaaaaa)
