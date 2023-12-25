Pytest Decorator’leri
Pytest, test fonksiyonlarına ek işlevsellik eklemek veya testlerin çalışmasını yönlendirmek için çeşitli dekoratörler sağlar. Bir dekoratör fonksiyon, genellikle orijinal fonksiyonun davranışını geliştiren veya değiştiren yeni bir fonksiyon döndüren bir başka fonksiyonu argüman olarak alır. 
Bu, fonksiyonların kaynak kodlarını doğrudan değiştirmeden işlevsellik eklemek için güçlü bir araç sağlar, böylece kodun yeniden kullanılabilir ve soyutlanabilir olmasını sağlar. 
Pytest'teki bazı önemli dekoratörler:
1.@pytest.fixture: Fixture'lar, test fonksiyonlarına örnek test verisi sağlayan veya test için ortamı kurmaya yarayan fonksiyonlardır. Pytest, kaynakları yönetmek için fixture'ları destekler. Pytest bir testi çalıştırmaya gittiğinde, 
o test fonksiyonunun imzasındaki parametrelere bakar ve sonra aynı isimlere sahip fixture'ları arar. 
Pytest bu fixture'ları bulduğunda onları çalıştırır, döndürdükleri değerleri (varsa) yakalar ve bu nesneleri test fonksiyonuna argüman olarak geçirir.
    @pytest.fixture
    def sample_data():
      return {'name': 'Eda', 'age': 29, 'email': 'eda@example.com'}
2.@pytest.mark.parametrize: @pytest.mark.parametrize, bir test fonksiyonunu belirli parametrelerle birden çok kez çalıştırarak çeşitli senaryoları test etmek için kullanılır.
Aşağıdaki örnekte test_addition fonksiyonu üç farklı parametre ile iki kez çalıştırılacaktır.      
  def add(x, y):
    return x + y
  @pytest.mark.parametrize("input1, input2, expected", [(1, 2, 3), (5, 5, 10)])
  def test_addition(input1, input2, expected):
    result = add(input1, input2)
    assert result == expected
3.@pytest.mark.skip: İlgili fonksiyonun geçici olarak atlanmasını sağlayarak test etmez. Aşağıdaki örnekte @pytest.mark.skip deklatörü ile test_feature fonksiyonu atlandığı için, pytest çıktısında bu testin "skipped" (atlandı) olarak işaretlendiğini görülür.
  @pytest.mark.skip(reason="Geçici olarak atlandı, çözüm bekleniyor.")
  def test_feature():
4.@pytest.mark.xfail: Bir testin beklenen bir şekilde başarısız olması durumunda başarılı sayılmasını sağlayan bir dekoratördür. Yani, test başarısız olursa, bu bir beklenen durum olarak işlenir ve test geçmiş olarak işaretlenir. 
Aşağıdaki örnekte test_feature fonksiyonu, @pytest.mark.xfail dekoratörü ile işaretlendi. Bu testin henüz uygulanmamış bir özelliği kontrol ettiğini ve başarısız olması bekleniyor olduğunu gösterir.
  @pytest.mark.xfail(reason="Henüz uygulanmamış özellik")
  def test_feature():

