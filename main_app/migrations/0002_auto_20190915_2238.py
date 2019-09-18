# Generated by Django 2.2.3 on 2019-09-15 22:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='City',
        ),
        migrations.AlterModelOptions(
            name='booking',
            options={'ordering': ['date']},
        ),
        migrations.AddField(
            model_name='booking',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='booking date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='experience',
            name='city',
            field=models.CharField(choices=[('Abidjan', 'Abidjan'), ('Accra', 'Accra'), ('Addis Ababa', 'Addis Ababa'), ('Ahmedabad', 'Ahmedabad'), ('Albuquerque', 'Albuquerque'), ('Aleppo', 'Aleppo'), ('Alexandria', 'Alexandria'), ('Algiers', 'Algiers'), ('Anaheim', 'Anaheim'), ('Anchorage', 'Anchorage'), ('Ankara', 'Ankara'), ('Arlington', 'Arlington'), ('Athens', 'Athens'), ('Atlanta', 'Atlanta'), ('Aurora', 'Aurora'), ('Austin', 'Austin'), ('Baghdad', 'Baghdad'), ('Bakersfield', 'Bakersfield'), ('Baku', 'Baku'), ('Baltimore', 'Baltimore'), ('Bandung', 'Bandung'), ('Bangalore', 'Bangalore'), ('Bangkok', 'Bangkok'), ('Barcelona', 'Barcelona'), ('Baton Rouge', 'Baton Rouge'), ('Beijing', 'Beijing'), ('Bekasi', 'Bekasi'), ('Belém', 'Belém'), ('Belo Horizonte', 'Belo Horizonte'), ('Benoni', 'Benoni'), ('Berlin', 'Berlin'), ('Birmingham', 'Birmingham'), ('Bogota', 'Bogota'), ('Boise', 'Boise'), ('Boston', 'Boston'), ('Brasília', 'Brasília'), ('Brooklyn', 'Brooklyn'), ('Buenos Aires', 'Buenos Aires'), ('Buffalo', 'Buffalo'), ('Busan', 'Busan'), ('Cairo', 'Cairo'), ('Cali', 'Cali'), ('Campinas', 'Campinas'), ('Cape Town', 'Cape Town'), ('Caracas', 'Caracas'), ('Casablanca', 'Casablanca'), ('Chandler', 'Chandler'), ('Changchun', 'Changchun'), ('Changsha', 'Changsha'), ('Charlotte', 'Charlotte'), ('Chengdu', 'Chengdu'), ('Chennai', 'Chennai'), ('Chesapeake', 'Chesapeake'), ('Chicago', 'Chicago'), ('Chittagong', 'Chittagong'), ('Chongqing', 'Chongqing'), ('Chula Vista', 'Chula Vista'), ('Cincinnati', 'Cincinnati'), ('Cleveland', 'Cleveland'), ('Colorado Springs', 'Colorado Springs'), ('Columbus', 'Columbus'), ('Corpus Christi', 'Corpus Christi'), ('Curitiba', 'Curitiba'), ('Daegu', 'Daegu'), ('Dakar', 'Dakar'), ('Dalian', 'Dalian'), ('Dallas', 'Dallas'), ('Damascus', 'Damascus'), ('Dar es Salaam', 'Dar es Salaam'), ('Delhi', 'Delhi'), ('Denver', 'Denver'), ('Detroit', 'Detroit'), ('Dhaka', 'Dhaka'), ('Dongguan', 'Dongguan'), ('Durban', 'Durban'), ('Durham', 'Durham'), ('El Giza', 'El Giza'), ('El Paso', 'El Paso'), ('Faisalabad', 'Faisalabad'), ('Fort Wayne', 'Fort Wayne'), ('Fort Worth', 'Fort Worth'), ('Fortaleza', 'Fortaleza'), ('Frankfurt', 'Frankfurt'), ('Fremont', 'Fremont'), ('Fresno', 'Fresno'), ('Fukuoka', 'Fukuoka'), ('Fuzhou', 'Fuzhou'), ('Garland', 'Garland'), ('George Town', 'George Town'), ('Gilbert', 'Gilbert'), ('Glendale', 'Glendale'), ('Greensboro', 'Greensboro'), ('Guadalajara', 'Guadalajara'), ('Guangzhou', 'Guangzhou'), ('Guayaquil', 'Guayaquil'), ('Guiyang', 'Guiyang'), ('Hangzhou', 'Hangzhou'), ('Hanoi', 'Hanoi'), ('Haora', 'Haora'), ('Harbin', 'Harbin'), ('Havana', 'Havana'), ('Hechi', 'Hechi'), ('Henderson', 'Henderson'), ('Hialeah', 'Hialeah'), ('Ho Chi Minh City', 'Ho Chi Minh City'), ('Hong Kong', 'Hong Kong'), ('Honolulu', 'Honolulu'), ('Houston', 'Houston'), ('Hyderabad', 'Hyderabad'), ('Ibadan', 'Ibadan'), ('Incheon', 'Incheon'), ('Indianapolis', 'Indianapolis'), ('Irvine', 'Irvine'), ('Irving', 'Irving'), ('Istanbul', 'Istanbul'), ('İzmir', 'İzmir'), ('Jacksonville', 'Jacksonville'), ('Jaipur', 'Jaipur'), ('Jakarta', 'Jakarta'), ('Jeddah', 'Jeddah'), ('Jersey City', 'Jersey City'), ('Jilin', 'Jilin'), ('Jinan', 'Jinan'), ('Jinxi', 'Jinxi'), ('Johannesburg', 'Johannesburg'), ('Kabul', 'Kabul'), ('Kano', 'Kano'), ('Kanpur', 'Kanpur'), ('Kansas City', 'Kansas City'), ('Kaohsiung', 'Kaohsiung'), ('Karachi', 'Karachi'), ('Katowice', 'Katowice'), ('Khartoum', 'Khartoum'), ('Kiev', 'Kiev'), ('Kinshasa', 'Kinshasa'), ('Kolkata', 'Kolkata'), ('Kunming', 'Kunming'), ('Lagos', 'Lagos'), ('Lahore', 'Lahore'), ('Lanzhou', 'Lanzhou'), ('Laredo', 'Laredo'), ('Las Vegas', 'Las Vegas'), ('Lexington', 'Lexington'), ('Lima', 'Lima'), ('Lincoln', 'Lincoln'), ('Lisbon', 'Lisbon'), ('London', 'London'), ('Long Beach', 'Long Beach'), ('Los Angeles', 'Los Angeles'), ('Louisville', 'Louisville'), ('Luanda', 'Luanda'), ('Lubbock', 'Lubbock'), ('Lucknow', 'Lucknow'), ('Madison', 'Madison'), ('Madrid', 'Madrid'), ('Manchester', 'Manchester'), ('Manila', 'Manila'), ('Mannheim', 'Mannheim'), ('Mashhad', 'Mashhad'), ('Medan', 'Medan'), ('Medellín', 'Medellín'), ('Melbourne', 'Melbourne'), ('Memphis', 'Memphis'), ('Mesa', 'Mesa'), ('Mexico City', 'Mexico City'), ('Miami', 'Miami'), ('Milan', 'Milan'), ('Milwaukee', 'Milwaukee'), ('Minneapolis', 'Minneapolis'), ('Monterrey', 'Monterrey'), ('Montréal', 'Montréal'), ('Moscow', 'Moscow'), ('Mumbai', 'Mumbai'), ('Nagoya', 'Nagoya'), ('Nagpur', 'Nagpur'), ('Nairobi', 'Nairobi'), ('Nanchang', 'Nanchang'), ('Nanchong', 'Nanchong'), ('Nanjing', 'Nanjing'), ('Nanning', 'Nanning'), ('Naples', 'Naples'), ('Nashville', 'Nashville'), ('New Orleans', 'New Orleans'), ('New York', 'New York'), ('Newark', 'Newark'), ('Norfolk', 'Norfolk'), ('North Las Vegas', 'North Las Vegas'), ('Oakland', 'Oakland'), ('Oklahoma City', 'Oklahoma City'), ('Omaha', 'Omaha'), ('Omdurman', 'Omdurman'), ('Orlando', 'Orlando'), ('Ōsaka', 'Ōsaka'), ('Paris', 'Paris'), ('Patna', 'Patna'), ('Philadelphia', 'Philadelphia'), ('Phoenix', 'Phoenix'), ('Pittsburgh', 'Pittsburgh'), ('Plano', 'Plano'), ('Portland', 'Portland'), ('Porto Alegre', 'Porto Alegre'), ('Puebla', 'Puebla'), ('Pune', 'Pune'), ('Pyongyang', 'Pyongyang'), ('Qingdao', 'Qingdao'), ('Queens', 'Queens'), ('Quezon City', 'Quezon City'), ('Raleigh', 'Raleigh'), ('Rangoon', 'Rangoon'), ('Recife', 'Recife'), ('Reno', 'Reno'), ('Richmond', 'Richmond'), ('Rio de Janeiro', 'Rio de Janeiro'), ('Riverside', 'Riverside'), ('Riyadh', 'Riyadh'), ('Rome', 'Rome'), ('Sacramento', 'Sacramento'), ('Saint Paul', 'Saint Paul'), ('Salvador', 'Salvador'), ('San Antonio', 'San Antonio'), ('San Diego', 'San Diego'), ('San Francisco', 'San Francisco'), ('San Jose', 'San Jose'), ('Santa Ana', 'Santa Ana'), ('Santa Cruz', 'Santa Cruz'), ('Santiago', 'Santiago'), ('Santo Domingo', 'Santo Domingo'), ('São Paulo', 'São Paulo'), ('Sapporo', 'Sapporo'), ('Scottsdale', 'Scottsdale'), ('Seattle', 'Seattle'), ('Sendai', 'Sendai'), ('Seoul', 'Seoul'), ('Shanghai', 'Shanghai'), ('Shenyeng', 'Shenyeng'), ('Shenzhen', 'Shenzhen'), ('Shijianzhuang', 'Shijianzhuang'), ('Singapore', 'Singapore'), ('Spokane', 'Spokane'), ('St. Louis', 'St. Louis'), ('St. Petersburg', 'St. Petersburg'), ('Stockton', 'Stockton'), ('Stuttgart', 'Stuttgart'), ('Surabaya', 'Surabaya'), ('Surat', 'Surat'), ('Sydney', 'Sydney'), ('Taichung', 'Taichung'), ('Taipei', 'Taipei'), ('Taiyuan', 'Taiyuan'), ('Tampa', 'Tampa'), ('Tashkent', 'Tashkent'), ('Tehran', 'Tehran'), ('Tel Aviv-Yafo', 'Tel Aviv-Yafo'), ('Tianjin', 'Tianjin'), ('Tokyo', 'Tokyo'), ('Toledo', 'Toledo'), ('Toronto', 'Toronto'), ('Tripoli', 'Tripoli'), ('Tucson', 'Tucson'), ('Tulsa', 'Tulsa'), ('Tunis', 'Tunis'), ('Ürümqi', 'Ürümqi'), ('Vancouver', 'Vancouver'), ('Vienna', 'Vienna'), ('Virginia Beach', 'Virginia Beach'), ('Washington', 'Washington'), ('Wenzhou', 'Wenzhou'), ('Wichita', 'Wichita'), ('Winston–Salem', 'Winston–Salem'), ('Wuhan', 'Wuhan'), ('Xiamen', 'Xiamen'), ('Xian', 'Xian'), ('Xiangtan', 'Xiangtan'), ('Yantai', 'Yantai'), ('Yokohama', 'Yokohama'), ('Zaozhuang', 'Zaozhuang'), ('Zhangzhou', 'Zhangzhou'), ('Zhengzhou', 'Zhengzhou'), ('Zibo', 'Zibo')], default='San Francisco', max_length=100),
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='experience',
            name='hours',
            field=models.IntegerField(choices=[(0, '12 AM'), (1, '1 AM'), (2, '2 AM'), (3, '3 AM'), (4, '4 AM'), (5, '5 AM'), (6, '6 AM'), (7, '7 AM'), (8, '8 AM'), (9, '9 AM'), (10, '10 AM'), (11, '11 AM'), (12, '12 PM'), (13, '1 PM'), (14, '2 PM'), (15, '3 PM'), (16, '4 PM'), (17, '5 PM'), (18, '6 PM'), (19, '7 PM'), (20, '8 PM'), (21, '9 PM'), (22, '10 PM'), (23, '11 PM')], default=12),
        ),
        migrations.AlterField(
            model_name='experience',
            name='language',
            field=models.CharField(choices=[('Albanian', 'Albanian'), ('Arabic', 'Arabic'), ('Austro-Bavarian', 'Austro-Bavarian'), ('Bengali', 'Bengali'), ('Bulgarian', 'Bulgarian'), ('Croatian', 'Croatian'), ('Czech', 'Czech'), ('Danish', 'Danish'), ('Dutch', 'Dutch'), ('English', 'English'), ('Finnish', 'Finnish'), ('French', 'French'), ('German', 'German'), ('Greek', 'Greek'), ('Hindi', 'Hindi'), ('Hungarian', 'Hungarian'), ('Italian', 'Italian'), ('Japanese', 'Japanese'), ('Javanese', 'Javanese'), ('Korean', 'Korean'), ('Lahnda', 'Lahnda'), ('Mandarin', 'Mandarin'), ('Marathi', 'Marathi'), ('Neapolitan', 'Neapolitan'), ('Norwegian', 'Norwegian'), ('Polish', 'Polish'), ('Portuguese', 'Portuguese'), ('Romanian', 'Romanian'), ('Russian', 'Russian'), ('Serbian', 'Serbian'), ('Slovak', 'Slovak'), ('Spanish', 'Spanish'), ('Swedish', 'Swedish'), ('Tamil', 'Tamil'), ('Telugu', 'Telugu'), ('Turkish', 'Turkish'), ('Ukrainian', 'Ukrainian'), ('Urdu', 'Urdu'), ('Vietnamese', 'Vietnamese')], default='English', max_length=100),
        ),
        migrations.AlterField(
            model_name='experience',
            name='minutes',
            field=models.IntegerField(choices=[(0, '00'), (15, '15'), (30, '30'), (45, '45')], default=0),
        ),
    ]