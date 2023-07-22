# Generated by Django 4.2.2 on 2023-07-15 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='pricing',
            name='from_district',
            field=models.CharField(blank=True, choices=[('Bagerhat', 'Bagerhat'), ('Bandarban', 'Bandarban'), ('Barguna', 'Barguna'), ('Barishal', 'Barishal'), ('Bhola', 'Bhola'), ('Bogura', 'Bogura'), ('Brahmanbaria', 'Brahmanbaria'), ('Chandpur', 'Chandpur'), ('Chattogram', 'Chattogram'), ('Chuadanga', 'Chuadanga'), ("Cox's Bazar", "Cox's Bazar"), ('Cumilla', 'Cumilla'), ('Dhaka', 'Dhaka'), ('Dinajpur', 'Dinajpur'), ('Faridpur', 'Faridpur'), ('Feni', 'Feni'), ('Gaibandha', 'Gaibandha'), ('Gazipur', 'Gazipur'), ('Gopalganj', 'Gopalganj'), ('Habiganj', 'Habiganj'), ('Jamalpur', 'Jamalpur'), ('Jashore', 'Jashore'), ('Jhalokati', 'Jhalokati'), ('Jhenaidah', 'Jhenaidah'), ('Joypurhat', 'Joypurhat'), ('Khagrachari', 'Khagrachari'), ('Khulna', 'Khulna'), ('Kishoreganj', 'Kishoreganj'), ('Kurigram', 'Kurigram'), ('Kushtia', 'Kushtia'), ('Lakshmipur', 'Lakshmipur'), ('Lalmonirhat', 'Lalmonirhat'), ('Madaripur', 'Madaripur'), ('Magura', 'Magura'), ('Manikganj', 'Manikganj'), ('Maulvibazar', 'Maulvibazar'), ('Meherpur', 'Meherpur'), ('Munshiganj', 'Munshiganj'), ('Mymensingh', 'Mymensingh'), ('Naogaon', 'Naogaon'), ('Narail', 'Narail'), ('Narayanganj', 'Narayanganj'), ('Narsingdi', 'Narsingdi'), ('Natore', 'Natore'), ('Nawabganj', 'Nawabganj'), ('Netrokona', 'Netrokona'), ('Nilphamari', 'Nilphamari'), ('Noakhali', 'Noakhali'), ('Pabna', 'Pabna'), ('Panchagarh', 'Panchagarh'), ('Patuakhali', 'Patuakhali'), ('Pirojpur', 'Pirojpur'), ('Rajbari', 'Rajbari'), ('Rajshahi', 'Rajshahi'), ('Rangamati', 'Rangamati'), ('Rangpur', 'Rangpur'), ('Satkhira', 'Satkhira'), ('Shariatpur', 'Shariatpur'), ('Sherpur', 'Sherpur'), ('Sirajgonj', 'Sirajgonj'), ('Sunamganj', 'Sunamganj'), ('Sylhet', 'Sylhet'), ('Tangail', 'Tangail'), ('Thakurgaon', 'Thakurgaon')], max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='pricing',
            name='from_division',
            field=models.CharField(blank=True, choices=[('Barishal', 'Barishal'), ('Chattogram', 'Chattogram'), ('Dhaka', 'Dhaka'), ('Khulna', 'Khulna'), ('Mymensingh', 'Mymensingh'), ('Rajshahi', 'Rajshahi'), ('Rangpur', 'Rangpur'), ('Sylhet', 'Sylhet')], max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='pricing',
            name='from_upazila',
            field=models.CharField(blank=True, choices=[('Abhaynagar', 'Abhaynagar'), ('Adamdighi', 'Adamdighi'), ('Aditmari', 'Aditmari'), ('Agailjhara', 'Agailjhara'), ('Ajmiriganj', 'Ajmiriganj'), ('Akhaura', 'Akhaura'), ('Akkelpur', 'Akkelpur'), ('Alamdanga', 'Alamdanga'), ('Alfadanga', 'Alfadanga'), ('Ali kadam', 'Ali kadam'), ('Amtali', 'Amtali'), ('Anwara', 'Anwara'), ('Araihazar', 'Araihazar'), ('Ashuganj', 'Ashuganj'), ('Assasuni', 'Assasuni'), ('Astagram', 'Astagram'), ('Atgharia', 'Atgharia'), ('Atpara Upazilla', 'Atpara Upazilla'), ('Atrai', 'Atrai'), ('Atwari', 'Atwari'), ('Babuganj', 'Babuganj'), ('Badalgachhi', 'Badalgachhi'), ('Badarganj', 'Badarganj'), ('Bagaichhari', 'Bagaichhari'), ('Bagatipara', 'Bagatipara'), ('Bagerhat Sadar', 'Bagerhat Sadar'), ('Bagha', 'Bagha'), ('Bagherpara', 'Bagherpara'), ('Bagmara', 'Bagmara'), ('Bahubal', 'Bahubal'), ('Bajitpur', 'Bajitpur'), ('Bakerganj', 'Bakerganj'), ('Baksiganj', 'Baksiganj'), ('Balaganj', 'Balaganj'), ('Baliadangi', 'Baliadangi'), ('Baliakandi', 'Baliakandi'), ('Bamna', 'Bamna'), ('Banaripara', 'Banaripara'), ('Bancharampur', 'Bancharampur'), ('Bandar', 'Bandar'), ('Bandarban Sadar', 'Bandarban Sadar'), ('Baniachang', 'Baniachang'), ('Banshkhali', 'Banshkhali'), ('Baraigram', 'Baraigram'), ('Baraigram', 'Baraigram'), ('Barguna Sadar', 'Barguna Sadar'), ('Barhatta Upazilla', 'Barhatta Upazilla'), ('Barisal Sadar', 'Barisal Sadar'), ('Barkal', 'Barkal'), ('Barlekha', 'Barlekha'), ('Barura', 'Barura'), ('Basail', 'Basail'), ('Batiaghata', 'Batiaghata'), ('Bauphal', 'Bauphal'), ('Beanibazar', 'Beanibazar'), ('Begumganj', 'Begumganj'), ('Belabo', 'Belabo'), ('Belaichhari', 'Belaichhari'), ('Belkuchi', 'Belkuchi'), ('Bera', 'Bera'), ('Betagi', 'Betagi'), ('Bhairab', 'Bhairab'), ('Bhaluka', 'Bhaluka'), ('Bhandaria', 'Bhandaria'), ('Bhanga', 'Bhanga'), ('Bhangura', 'Bhangura'), ('Bhedarganj', 'Bhedarganj'), ('Bheramara', 'Bheramara'), ('Bhola Sadar', 'Bhola Sadar'), ('Bholahat', 'Bholahat'), ('Bhuapur', 'Bhuapur'), ('Bhurungamari', 'Bhurungamari'), ('Bijoynagar', 'Bijoynagar'), ('Biral', 'Biral'), ('Birampur', 'Birampur'), ('Birganj', 'Birganj'), ('Bishwamvarpur', 'Bishwamvarpur'), ('Bishwanath', 'Bishwanath'), ('Boalkhali', 'Boalkhali'), ('Boalmari', 'Boalmari'), ('Bochaganj', 'Bochaganj'), ('Boda', 'Boda'), ('Bogra Sadar', 'Bogra Sadar'), ('Brahmanbaria Sadar', 'Brahmanbaria Sadar'), ('Brahmanpara', 'Brahmanpara'), ('Burhanuddin', 'Burhanuddin'), ('Burichong', 'Burichong'), ('Chagalnaiya', 'Chagalnaiya'), ('Chakaria', 'Chakaria'), ('Chandanaish', 'Chandanaish'), ('Chandina', 'Chandina'), ('Chandpur Sadar', 'Chandpur Sadar'), ('Char Fasson', 'Char Fasson'), ('Char Rajibpur', 'Char Rajibpur'), ('Charbhadrasan', 'Charbhadrasan'), ('Charghat', 'Charghat'), ('Chatkhil', 'Chatkhil'), ('Chatmohar', 'Chatmohar'), ('Chauddagram', 'Chauddagram'), ('Chaugachha', 'Chaugachha'), ('Chauhali', 'Chauhali'), ('Chhatak', 'Chhatak'), ('Chilmari', 'Chilmari'), ('Chirirbandar', 'Chirirbandar'), ('Chitalmari', 'Chitalmari'), ('Chuadanga-S', 'Chuadanga-S'), ('Chunarughat', 'Chunarughat'), ('Comilla Sadar', 'Comilla Sadar'), ('Comilla Sadar South', 'Comilla Sadar South'), ('Companiganj', 'Companiganj'), ('Companyganj', 'Companyganj'), ('Dacope', 'Dacope'), ('Daganbhyan', 'Daganbhyan'), ('Dakshin Surma', 'Dakshin Surma'), ('Damudya', 'Damudya'), ('Damurhuda', 'Damurhuda'), ('Dasar', 'Dasar'), ('Dashmina', 'Dashmina'), ('Daudkandi', 'Daudkandi'), ('Daulatkhan', 'Daulatkhan'), ('Daulatpur', 'Daulatpur'), ('Daulatpur', 'Daulatpur'), ('Debhata', 'Debhata'), ('Debidwar', 'Debidwar'), ('Debiganj', 'Debiganj'), ('Delduar', 'Delduar'), ('Derai', 'Derai'), ('Dewanganj', 'Dewanganj'), ('Dhamoirhat', 'Dhamoirhat'), ('Dhamrai', 'Dhamrai'), ('Dhanbari', 'Dhanbari'), ('Dharampasha', 'Dharampasha'), ('Dhobaura', 'Dhobaura'), ('Dhunat', 'Dhunat'), ('Dhupchanchia', 'Dhupchanchia'), ('Dighalia', 'Dighalia'), ('Dighinala', 'Dighinala'), ('Dimla', 'Dimla'), ('Dinajpur Sadar', 'Dinajpur Sadar'), ('Dohar', 'Dohar'), ('Domar', 'Domar'), ('Dowarabazar', 'Dowarabazar'), ('Dumki', 'Dumki'), ('Dumuria', 'Dumuria'), ('Durgapur', 'Durgapur'), ('Durgapur Upazilla', 'Durgapur Upazilla'), ('Eidgaon', 'Eidgaon'), ('Fakirhat', 'Fakirhat'), ('Faridganj', 'Faridganj'), ('Faridpur', 'Faridpur'), ('Faridpur Sadar', 'Faridpur Sadar'), ('Fatikchhari', 'Fatikchhari'), ('Fenchuganj', 'Fenchuganj'), ('Feni Sadar', 'Feni Sadar'), ('Fhulgazi', 'Fhulgazi'), ('Fulbaria', 'Fulbaria'), ('Fulchhari', 'Fulchhari'), ('Gabtali', 'Gabtali'), ('Gaffargaon', 'Gaffargaon'), ('Gaibandha sadar', 'Gaibandha sadar'), ('Galachipa', 'Galachipa'), ('Gangachara', 'Gangachara'), ('Gauripur', 'Gauripur'), ('Gaurnadi', 'Gaurnadi'), ('Gazaria', 'Gazaria'), ('Gazipur Sadar-Joydebpur', 'Gazipur Sadar-Joydebpur'), ('Ghatail', 'Ghatail'), ('Ghior', 'Ghior'), ('Ghoraghat', 'Ghoraghat'), ('Goalandaghat', 'Goalandaghat'), ('Gobindaganj', 'Gobindaganj'), ('Godagari', 'Godagari'), ('Golapganj', 'Golapganj'), ('Gomastapur', 'Gomastapur'), ('Gopalganj Sadar', 'Gopalganj Sadar'), ('Gopalpur', 'Gopalpur'), ('Gosairhat', 'Gosairhat'), ('Gowainghat', 'Gowainghat'), ('Habiganj Sadar', 'Habiganj Sadar'), ('Haimchar', 'Haimchar'), ('Hakimpur', 'Hakimpur'), ('Haluaghat', 'Haluaghat'), ('Harinakunda', 'Harinakunda'), ('Haripur', 'Haripur'), ('Harirampur', 'Harirampur'), ('Hathazari', 'Hathazari'), ('Hatia', 'Hatia'), ('Hatibandha', 'Hatibandha'), ('Haziganj', 'Haziganj'), ('Hizla', 'Hizla'), ('Homna', 'Homna'), ('Hossainpur', 'Hossainpur'), ('Ishwardi', 'Ishwardi'), ('Ishwarganj', 'Ishwarganj'), ('Islampur', 'Islampur'), ('Itna', 'Itna'), ('Jagannathpur', 'Jagannathpur'), ('Jajira', 'Jajira'), ('Jaldhaka', 'Jaldhaka'), ('Jamalganj', 'Jamalganj'), ('Jamalpur Sadar', 'Jamalpur Sadar'), ('Jessore Sadar', 'Jessore Sadar'), ('Jhalokati Sadar', 'Jhalokati Sadar'), ('Jhenaidah Sadar', 'Jhenaidah Sadar'), ('Jhenaigati', 'Jhenaigati'), ('Jhikargachha', 'Jhikargachha'), ('Jibannagar', 'Jibannagar'), ('Jointapur', 'Jointapur'), ('Joypurhat S', 'Joypurhat S'), ('Juraichhari', 'Juraichhari'), ('Juri', 'Juri'), ('Kachua', 'Kachua'), ('Kachua', 'Kachua'), ('Kahaloo', 'Kahaloo'), ('Kaharole', 'Kaharole'), ('Kalai', 'Kalai'), ('Kalapara', 'Kalapara'), ('Kalaroa', 'Kalaroa'), ('Kalia Upazilla', 'Kalia Upazilla'), ('Kaliakior', 'Kaliakior'), ('Kaliganj', 'Kaliganj'), ('Kaliganj', 'Kaliganj'), ('Kaliganj', 'Kaliganj'), ('Kaliganj', 'Kaliganj'), ('Kalihati', 'Kalihati'), ('Kalkini', 'Kalkini'), ('Kalmakanda Upazilla', 'Kalmakanda Upazilla'), ('Kalukhali', 'Kalukhali'), ('Kamalganj', 'Kamalganj'), ('Kamarkhanda', 'Kamarkhanda'), ('Kanaighat', 'Kanaighat'), ('Kapasia', 'Kapasia'), ('Kaptai', 'Kaptai'), ('Karimganj', 'Karimganj'), ('Kasba', 'Kasba'), ('Kashiani', 'Kashiani'), ('Kathalia', 'Kathalia'), ('Katiadi', 'Katiadi'), ('Kaukhali', 'Kaukhali'), ('Kaukhali', 'Kaukhali'), ('Kaunia', 'Kaunia'), ('Kazipur', 'Kazipur'), ('Kendua Upazilla', 'Kendua Upazilla'), ('Keraniganj', 'Keraniganj'), ('Keshabpur', 'Keshabpur'), ('Khagrachhari', 'Khagrachhari'), ('Khaliajuri Upazilla', 'Khaliajuri Upazilla'), ('Khansama', 'Khansama'), ('Khetlal', 'Khetlal'), ('Khoksa', 'Khoksa'), ('Kishoreganj', 'Kishoreganj'), ('Kishoreganj Sadar', 'Kishoreganj Sadar'), ('Kobirhat', 'Kobirhat'), ('Komol Nagar', 'Komol Nagar'), ('Kotalipara', 'Kotalipara'), ('Kotchandpur', 'Kotchandpur'), ('Koyra', 'Koyra'), ('Kulaura', 'Kulaura'), ('Kuliarchar', 'Kuliarchar'), ('Kumarkhali', 'Kumarkhali'), ('Kurigram Sadar', 'Kurigram Sadar'), ('Kushtia Sadar', 'Kushtia Sadar'), ('Kutubdia', 'Kutubdia'), ('Lakhai', 'Lakhai'), ('Laksam', 'Laksam'), ('Lakshmichhari', 'Lakshmichhari'), ('Lakshmipur Sadar', 'Lakshmipur Sadar'), ('Lalmanirhat Sadar', 'Lalmanirhat Sadar'), ('Lalmohan', 'Lalmohan'), ('Lalpur', 'Lalpur'), ('Lama', 'Lama'), ('Langadu', 'Langadu'), ('Lohagara', 'Lohagara'), ('Lohagara Upazilla', 'Lohagara Upazilla'), ('Lohajang', 'Lohajang'), ('Madan Upazilla', 'Madan Upazilla'), ('Madarganj', 'Madarganj'), ('Madaripur Sadar', 'Madaripur Sadar'), ('Madhabpur', 'Madhabpur'), ('Madhukhali', 'Madhukhali'), ('Madhupur', 'Madhupur'), ('Magura Sadar', 'Magura Sadar'), ('Mahalchhari', 'Mahalchhari'), ('Maheshkhali', 'Maheshkhali'), ('Maheshpur', 'Maheshpur'), ('Manda', 'Manda'), ('Manikchhari', 'Manikchhari'), ('Manikganj Sadar', 'Manikganj Sadar'), ('Manirampur', 'Manirampur'), ('Manpura', 'Manpura'), ('Mathbaria', 'Mathbaria'), ('Matiranga', 'Matiranga'), ('Matlab Dakkhin', 'Matlab Dakkhin'), ('Matlab Uttar', 'Matlab Uttar'), ('Meghna', 'Meghna'), ('Mehendiganj', 'Mehendiganj'), ('Meherpur-S', 'Meherpur-S'), ('Melandaha', 'Melandaha'), ('Mirpur', 'Mirpur'), ('Mirsharai', 'Mirsharai'), ('Mirzaganj', 'Mirzaganj'), ('Mirzapur', 'Mirzapur'), ('Mithamain', 'Mithamain'), ('Mithapukur', 'Mithapukur'), ('Modhyanagar', 'Modhyanagar'), ('Mohadevpur', 'Mohadevpur'), ('Mohammadpur', 'Mohammadpur'), ('Mohanganj Upazilla', 'Mohanganj Upazilla'), ('Mohanpur', 'Mohanpur'), ('Mollahat', 'Mollahat'), ('Mongla', 'Mongla'), ('Monohardi', 'Monohardi'), ('Monohorgonj', 'Monohorgonj'), ('Morrelganj', 'Morrelganj'), ('Moulvibazar Sadar', 'Moulvibazar Sadar'), ('Mujib Nagar', 'Mujib Nagar'), ('Muksudpur', 'Muksudpur'), ('Muktagachha', 'Muktagachha'), ('Muladi', 'Muladi'), ('Munshiganj Sadar', 'Munshiganj Sadar'), ('Muradnagar', 'Muradnagar'), ('Mymensingh Sadar', 'Mymensingh Sadar'), ('Nabiganj', 'Nabiganj'), ('Nabinagar', 'Nabinagar'), ('Nachole', 'Nachole'), ('Nagarkanda', 'Nagarkanda'), ('Nagarpur', 'Nagarpur'), ('Nageshwari', 'Nageshwari'), ('Naikhongchhari', 'Naikhongchhari'), ('Nakla', 'Nakla'), ('Nalchity', 'Nalchity'), ('Nalitabari', 'Nalitabari'), ('Nandail', 'Nandail'), ('Nandigram', 'Nandigram'), ('Nangalkot', 'Nangalkot'), ('Nannerchar', 'Nannerchar'), ('Naogaon Sadar', 'Naogaon Sadar'), ('Narail-S Upazilla', 'Narail-S Upazilla'), ('Naria', 'Naria'), ('Narsingdi Sadar', 'Narsingdi Sadar'), ('Narundi Police I.C', 'Narundi Police I.C'), ('Naryanganj Sadar', 'Naryanganj Sadar'), ('Nasirnagar', 'Nasirnagar'), ('Natore Sadar', 'Natore Sadar'), ('Natore Sadar', 'Natore Sadar'), ('Nawabganj', 'Nawabganj'), ('Nawabganj', 'Nawabganj'), ('Nawabganj Sadar', 'Nawabganj Sadar'), ('Nazirpur', 'Nazirpur'), ('Nesarabad', 'Nesarabad'), ('Netrakona-S Upazilla', 'Netrakona-S Upazilla'), ('Niamatpur', 'Niamatpur'), ('Nikli', 'Nikli'), ('Nilphamari Sadar', 'Nilphamari Sadar'), ('Noakhali Sadar', 'Noakhali Sadar'), ('Nobigonj', 'Nobigonj'), ('Paba', 'Paba'), ('Pabna Sadar', 'Pabna Sadar'), ('Paikgachha', 'Paikgachha'), ('Pakundia', 'Pakundia'), ('Palash', 'Palash'), ('Palashbari', 'Palashbari'), ('Panchagarh Sadar', 'Panchagarh Sadar'), ('Panchbibi', 'Panchbibi'), ('Panchhari', 'Panchhari'), ('Pangsha', 'Pangsha'), ('Parbatipur', 'Parbatipur'), ('Parshuram', 'Parshuram'), ('Patgram', 'Patgram'), ('Patharghata', 'Patharghata'), ('Patiya', 'Patiya'), ('Patnitala', 'Patnitala'), ('Patuakhali Sadar', 'Patuakhali Sadar'), ('Pekua', 'Pekua'), ('Phulbari', 'Phulbari'), ('Phulbari', 'Phulbari'), ('Phulpur', 'Phulpur'), ('Phultala', 'Phultala'), ('Pirgachha', 'Pirgachha'), ('Pirganj', 'Pirganj'), ('Pirganj', 'Pirganj'), ('Pirojpur Sadar', 'Pirojpur Sadar'), ('Porsha', 'Porsha'), ('Purbadhala Upazilla', 'Purbadhala Upazilla'), ('Puthia', 'Puthia'), ('Raiganj', 'Raiganj'), ('Raipur', 'Raipur'), ('Raipura, Narsingdi', 'Raipura, Narsingdi'), ('Rajapur', 'Rajapur'), ('Rajarhat', 'Rajarhat'), ('Rajasthali', 'Rajasthali'), ('Rajbari Sadar', 'Rajbari Sadar'), ('Rajnagar', 'Rajnagar'), ('Rajoir', 'Rajoir'), ('Ramganj', 'Ramganj'), ('Ramgarh', 'Ramgarh'), ('Ramgati', 'Ramgati'), ('Rampal', 'Rampal'), ('Ramu', 'Ramu'), ('Rangabali', 'Rangabali'), ('Rangamati Sadar', 'Rangamati Sadar'), ('Rangpur Sadar', 'Rangpur Sadar'), ('Rangunia', 'Rangunia'), ('Raninagar', 'Raninagar'), ('Ranisankail', 'Ranisankail'), ('Raozan', 'Raozan'), ('Rowangchhari', 'Rowangchhari'), ('Rowmari', 'Rowmari'), ('Ruma', 'Ruma'), ('Rupganj', 'Rupganj'), ('Rupsa', 'Rupsa'), ('Sadarpur', 'Sadarpur'), ('Sadullapur', 'Sadullapur'), ('Saghata', 'Saghata'), ('Sahajanpur', 'Sahajanpur'), ('Saidpur', 'Saidpur'), ('Sakhipur', 'Sakhipur'), ('Sandwip', 'Sandwip'), ('Santhia', 'Santhia'), ('Sapahar', 'Sapahar'), ('Sarail', 'Sarail'), ('Sarankhola', 'Sarankhola'), ('Sariakandi', 'Sariakandi'), ('Sarishabari', 'Sarishabari'), ('Satkania', 'Satkania'), ('Satkhira Sadar', 'Satkhira Sadar'), ('Saturia', 'Saturia'), ('Savar', 'Savar'), ('Shahbazpur Town', 'Shahbazpur Town'), ('Shahjadpur', 'Shahjadpur'), ('Shahrasti', 'Shahrasti'), ('Shailkupa', 'Shailkupa'), ('Shaistagonj', 'Shaistagonj'), ('Shalikha', 'Shalikha'), ('Shaltha', 'Shaltha'), ('Shanthiganj', 'Shanthiganj'), ('Shariatpur Sadar -Palong', 'Shariatpur Sadar -Palong'), ('Sharsha', 'Sharsha'), ('Shenbag', 'Shenbag'), ('Sherpur', 'Sherpur'), ('Sherpur Sadar', 'Sherpur Sadar'), ('Shibalaya', 'Shibalaya'), ('Shibchar', 'Shibchar'), ('Shibganj', 'Shibganj'), ('Shibganj', 'Shibganj'), ('Shibpur', 'Shibpur'), ('Shyamnagar', 'Shyamnagar'), ('Siddirgonj', 'Siddirgonj'), ('Singair', 'Singair'), ('Sirajdikhan', 'Sirajdikhan'), ('Sirajganj Sadar', 'Sirajganj Sadar'), ('Sitakunda', 'Sitakunda'), ('Sonagazi', 'Sonagazi'), ('Sonaimuri', 'Sonaimuri'), ('Sonargaon', 'Sonargaon'), ('Sonatala', 'Sonatala'), ('Sreebardi', 'Sreebardi'), ('Sreemangal', 'Sreemangal'), ('Sreenagar', 'Sreenagar'), ('Sreepur', 'Sreepur'), ('Sripur', 'Sripur'), ('Suborno Char', 'Suborno Char'), ('Sujanagar', 'Sujanagar'), ('Sulla', 'Sulla'), ('Sunamganj Sadar', 'Sunamganj Sadar'), ('Sundarganj', 'Sundarganj'), ('Sylhet Sadar', 'Sylhet Sadar'), ('Tahirpur', 'Tahirpur'), ('Tala', 'Tala'), ('Taltali', 'Taltali'), ('Tangail Sadar', 'Tangail Sadar'), ('Tanore', 'Tanore'), ('Taraganj', 'Taraganj'), ('Tarail', 'Tarail'), ('Tarash', 'Tarash'), ('Tazumuddin', 'Tazumuddin'), ('Teknaf', 'Teknaf'), ('Terokhada', 'Terokhada'), ('Tetulia', 'Tetulia'), ('Thakurgaon Sadar', 'Thakurgaon Sadar'), ('Thanchi', 'Thanchi'), ('Titas', 'Titas'), ('Tongi', 'Tongi'), ('Tongibari', 'Tongibari'), ('Trishal', 'Trishal'), ('Tungipara', 'Tungipara'), ('Ukhia', 'Ukhia'), ('Ulipur', 'Ulipur'), ('Ullahpara', 'Ullahpara'), ('Wazirpur', 'Wazirpur'), ('Zakiganj', 'Zakiganj'), ('Zianagar', 'Zianagar'), ('angni', 'angni'), ("{{198}}''{{199}}", "{{198}}''{{199}}")], max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='pricing',
            name='to_district',
            field=models.CharField(blank=True, choices=[('Bagerhat', 'Bagerhat'), ('Bandarban', 'Bandarban'), ('Barguna', 'Barguna'), ('Barishal', 'Barishal'), ('Bhola', 'Bhola'), ('Bogura', 'Bogura'), ('Brahmanbaria', 'Brahmanbaria'), ('Chandpur', 'Chandpur'), ('Chattogram', 'Chattogram'), ('Chuadanga', 'Chuadanga'), ("Cox's Bazar", "Cox's Bazar"), ('Cumilla', 'Cumilla'), ('Dhaka', 'Dhaka'), ('Dinajpur', 'Dinajpur'), ('Faridpur', 'Faridpur'), ('Feni', 'Feni'), ('Gaibandha', 'Gaibandha'), ('Gazipur', 'Gazipur'), ('Gopalganj', 'Gopalganj'), ('Habiganj', 'Habiganj'), ('Jamalpur', 'Jamalpur'), ('Jashore', 'Jashore'), ('Jhalokati', 'Jhalokati'), ('Jhenaidah', 'Jhenaidah'), ('Joypurhat', 'Joypurhat'), ('Khagrachari', 'Khagrachari'), ('Khulna', 'Khulna'), ('Kishoreganj', 'Kishoreganj'), ('Kurigram', 'Kurigram'), ('Kushtia', 'Kushtia'), ('Lakshmipur', 'Lakshmipur'), ('Lalmonirhat', 'Lalmonirhat'), ('Madaripur', 'Madaripur'), ('Magura', 'Magura'), ('Manikganj', 'Manikganj'), ('Maulvibazar', 'Maulvibazar'), ('Meherpur', 'Meherpur'), ('Munshiganj', 'Munshiganj'), ('Mymensingh', 'Mymensingh'), ('Naogaon', 'Naogaon'), ('Narail', 'Narail'), ('Narayanganj', 'Narayanganj'), ('Narsingdi', 'Narsingdi'), ('Natore', 'Natore'), ('Nawabganj', 'Nawabganj'), ('Netrokona', 'Netrokona'), ('Nilphamari', 'Nilphamari'), ('Noakhali', 'Noakhali'), ('Pabna', 'Pabna'), ('Panchagarh', 'Panchagarh'), ('Patuakhali', 'Patuakhali'), ('Pirojpur', 'Pirojpur'), ('Rajbari', 'Rajbari'), ('Rajshahi', 'Rajshahi'), ('Rangamati', 'Rangamati'), ('Rangpur', 'Rangpur'), ('Satkhira', 'Satkhira'), ('Shariatpur', 'Shariatpur'), ('Sherpur', 'Sherpur'), ('Sirajgonj', 'Sirajgonj'), ('Sunamganj', 'Sunamganj'), ('Sylhet', 'Sylhet'), ('Tangail', 'Tangail'), ('Thakurgaon', 'Thakurgaon')], max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='pricing',
            name='to_division',
            field=models.CharField(blank=True, choices=[('Barishal', 'Barishal'), ('Chattogram', 'Chattogram'), ('Dhaka', 'Dhaka'), ('Khulna', 'Khulna'), ('Mymensingh', 'Mymensingh'), ('Rajshahi', 'Rajshahi'), ('Rangpur', 'Rangpur'), ('Sylhet', 'Sylhet')], max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='pricing',
            name='to_upazila',
            field=models.CharField(blank=True, choices=[('Abhaynagar', 'Abhaynagar'), ('Adamdighi', 'Adamdighi'), ('Aditmari', 'Aditmari'), ('Agailjhara', 'Agailjhara'), ('Ajmiriganj', 'Ajmiriganj'), ('Akhaura', 'Akhaura'), ('Akkelpur', 'Akkelpur'), ('Alamdanga', 'Alamdanga'), ('Alfadanga', 'Alfadanga'), ('Ali kadam', 'Ali kadam'), ('Amtali', 'Amtali'), ('Anwara', 'Anwara'), ('Araihazar', 'Araihazar'), ('Ashuganj', 'Ashuganj'), ('Assasuni', 'Assasuni'), ('Astagram', 'Astagram'), ('Atgharia', 'Atgharia'), ('Atpara Upazilla', 'Atpara Upazilla'), ('Atrai', 'Atrai'), ('Atwari', 'Atwari'), ('Babuganj', 'Babuganj'), ('Badalgachhi', 'Badalgachhi'), ('Badarganj', 'Badarganj'), ('Bagaichhari', 'Bagaichhari'), ('Bagatipara', 'Bagatipara'), ('Bagerhat Sadar', 'Bagerhat Sadar'), ('Bagha', 'Bagha'), ('Bagherpara', 'Bagherpara'), ('Bagmara', 'Bagmara'), ('Bahubal', 'Bahubal'), ('Bajitpur', 'Bajitpur'), ('Bakerganj', 'Bakerganj'), ('Baksiganj', 'Baksiganj'), ('Balaganj', 'Balaganj'), ('Baliadangi', 'Baliadangi'), ('Baliakandi', 'Baliakandi'), ('Bamna', 'Bamna'), ('Banaripara', 'Banaripara'), ('Bancharampur', 'Bancharampur'), ('Bandar', 'Bandar'), ('Bandarban Sadar', 'Bandarban Sadar'), ('Baniachang', 'Baniachang'), ('Banshkhali', 'Banshkhali'), ('Baraigram', 'Baraigram'), ('Baraigram', 'Baraigram'), ('Barguna Sadar', 'Barguna Sadar'), ('Barhatta Upazilla', 'Barhatta Upazilla'), ('Barisal Sadar', 'Barisal Sadar'), ('Barkal', 'Barkal'), ('Barlekha', 'Barlekha'), ('Barura', 'Barura'), ('Basail', 'Basail'), ('Batiaghata', 'Batiaghata'), ('Bauphal', 'Bauphal'), ('Beanibazar', 'Beanibazar'), ('Begumganj', 'Begumganj'), ('Belabo', 'Belabo'), ('Belaichhari', 'Belaichhari'), ('Belkuchi', 'Belkuchi'), ('Bera', 'Bera'), ('Betagi', 'Betagi'), ('Bhairab', 'Bhairab'), ('Bhaluka', 'Bhaluka'), ('Bhandaria', 'Bhandaria'), ('Bhanga', 'Bhanga'), ('Bhangura', 'Bhangura'), ('Bhedarganj', 'Bhedarganj'), ('Bheramara', 'Bheramara'), ('Bhola Sadar', 'Bhola Sadar'), ('Bholahat', 'Bholahat'), ('Bhuapur', 'Bhuapur'), ('Bhurungamari', 'Bhurungamari'), ('Bijoynagar', 'Bijoynagar'), ('Biral', 'Biral'), ('Birampur', 'Birampur'), ('Birganj', 'Birganj'), ('Bishwamvarpur', 'Bishwamvarpur'), ('Bishwanath', 'Bishwanath'), ('Boalkhali', 'Boalkhali'), ('Boalmari', 'Boalmari'), ('Bochaganj', 'Bochaganj'), ('Boda', 'Boda'), ('Bogra Sadar', 'Bogra Sadar'), ('Brahmanbaria Sadar', 'Brahmanbaria Sadar'), ('Brahmanpara', 'Brahmanpara'), ('Burhanuddin', 'Burhanuddin'), ('Burichong', 'Burichong'), ('Chagalnaiya', 'Chagalnaiya'), ('Chakaria', 'Chakaria'), ('Chandanaish', 'Chandanaish'), ('Chandina', 'Chandina'), ('Chandpur Sadar', 'Chandpur Sadar'), ('Char Fasson', 'Char Fasson'), ('Char Rajibpur', 'Char Rajibpur'), ('Charbhadrasan', 'Charbhadrasan'), ('Charghat', 'Charghat'), ('Chatkhil', 'Chatkhil'), ('Chatmohar', 'Chatmohar'), ('Chauddagram', 'Chauddagram'), ('Chaugachha', 'Chaugachha'), ('Chauhali', 'Chauhali'), ('Chhatak', 'Chhatak'), ('Chilmari', 'Chilmari'), ('Chirirbandar', 'Chirirbandar'), ('Chitalmari', 'Chitalmari'), ('Chuadanga-S', 'Chuadanga-S'), ('Chunarughat', 'Chunarughat'), ('Comilla Sadar', 'Comilla Sadar'), ('Comilla Sadar South', 'Comilla Sadar South'), ('Companiganj', 'Companiganj'), ('Companyganj', 'Companyganj'), ('Dacope', 'Dacope'), ('Daganbhyan', 'Daganbhyan'), ('Dakshin Surma', 'Dakshin Surma'), ('Damudya', 'Damudya'), ('Damurhuda', 'Damurhuda'), ('Dasar', 'Dasar'), ('Dashmina', 'Dashmina'), ('Daudkandi', 'Daudkandi'), ('Daulatkhan', 'Daulatkhan'), ('Daulatpur', 'Daulatpur'), ('Daulatpur', 'Daulatpur'), ('Debhata', 'Debhata'), ('Debidwar', 'Debidwar'), ('Debiganj', 'Debiganj'), ('Delduar', 'Delduar'), ('Derai', 'Derai'), ('Dewanganj', 'Dewanganj'), ('Dhamoirhat', 'Dhamoirhat'), ('Dhamrai', 'Dhamrai'), ('Dhanbari', 'Dhanbari'), ('Dharampasha', 'Dharampasha'), ('Dhobaura', 'Dhobaura'), ('Dhunat', 'Dhunat'), ('Dhupchanchia', 'Dhupchanchia'), ('Dighalia', 'Dighalia'), ('Dighinala', 'Dighinala'), ('Dimla', 'Dimla'), ('Dinajpur Sadar', 'Dinajpur Sadar'), ('Dohar', 'Dohar'), ('Domar', 'Domar'), ('Dowarabazar', 'Dowarabazar'), ('Dumki', 'Dumki'), ('Dumuria', 'Dumuria'), ('Durgapur', 'Durgapur'), ('Durgapur Upazilla', 'Durgapur Upazilla'), ('Eidgaon', 'Eidgaon'), ('Fakirhat', 'Fakirhat'), ('Faridganj', 'Faridganj'), ('Faridpur', 'Faridpur'), ('Faridpur Sadar', 'Faridpur Sadar'), ('Fatikchhari', 'Fatikchhari'), ('Fenchuganj', 'Fenchuganj'), ('Feni Sadar', 'Feni Sadar'), ('Fhulgazi', 'Fhulgazi'), ('Fulbaria', 'Fulbaria'), ('Fulchhari', 'Fulchhari'), ('Gabtali', 'Gabtali'), ('Gaffargaon', 'Gaffargaon'), ('Gaibandha sadar', 'Gaibandha sadar'), ('Galachipa', 'Galachipa'), ('Gangachara', 'Gangachara'), ('Gauripur', 'Gauripur'), ('Gaurnadi', 'Gaurnadi'), ('Gazaria', 'Gazaria'), ('Gazipur Sadar-Joydebpur', 'Gazipur Sadar-Joydebpur'), ('Ghatail', 'Ghatail'), ('Ghior', 'Ghior'), ('Ghoraghat', 'Ghoraghat'), ('Goalandaghat', 'Goalandaghat'), ('Gobindaganj', 'Gobindaganj'), ('Godagari', 'Godagari'), ('Golapganj', 'Golapganj'), ('Gomastapur', 'Gomastapur'), ('Gopalganj Sadar', 'Gopalganj Sadar'), ('Gopalpur', 'Gopalpur'), ('Gosairhat', 'Gosairhat'), ('Gowainghat', 'Gowainghat'), ('Habiganj Sadar', 'Habiganj Sadar'), ('Haimchar', 'Haimchar'), ('Hakimpur', 'Hakimpur'), ('Haluaghat', 'Haluaghat'), ('Harinakunda', 'Harinakunda'), ('Haripur', 'Haripur'), ('Harirampur', 'Harirampur'), ('Hathazari', 'Hathazari'), ('Hatia', 'Hatia'), ('Hatibandha', 'Hatibandha'), ('Haziganj', 'Haziganj'), ('Hizla', 'Hizla'), ('Homna', 'Homna'), ('Hossainpur', 'Hossainpur'), ('Ishwardi', 'Ishwardi'), ('Ishwarganj', 'Ishwarganj'), ('Islampur', 'Islampur'), ('Itna', 'Itna'), ('Jagannathpur', 'Jagannathpur'), ('Jajira', 'Jajira'), ('Jaldhaka', 'Jaldhaka'), ('Jamalganj', 'Jamalganj'), ('Jamalpur Sadar', 'Jamalpur Sadar'), ('Jessore Sadar', 'Jessore Sadar'), ('Jhalokati Sadar', 'Jhalokati Sadar'), ('Jhenaidah Sadar', 'Jhenaidah Sadar'), ('Jhenaigati', 'Jhenaigati'), ('Jhikargachha', 'Jhikargachha'), ('Jibannagar', 'Jibannagar'), ('Jointapur', 'Jointapur'), ('Joypurhat S', 'Joypurhat S'), ('Juraichhari', 'Juraichhari'), ('Juri', 'Juri'), ('Kachua', 'Kachua'), ('Kachua', 'Kachua'), ('Kahaloo', 'Kahaloo'), ('Kaharole', 'Kaharole'), ('Kalai', 'Kalai'), ('Kalapara', 'Kalapara'), ('Kalaroa', 'Kalaroa'), ('Kalia Upazilla', 'Kalia Upazilla'), ('Kaliakior', 'Kaliakior'), ('Kaliganj', 'Kaliganj'), ('Kaliganj', 'Kaliganj'), ('Kaliganj', 'Kaliganj'), ('Kaliganj', 'Kaliganj'), ('Kalihati', 'Kalihati'), ('Kalkini', 'Kalkini'), ('Kalmakanda Upazilla', 'Kalmakanda Upazilla'), ('Kalukhali', 'Kalukhali'), ('Kamalganj', 'Kamalganj'), ('Kamarkhanda', 'Kamarkhanda'), ('Kanaighat', 'Kanaighat'), ('Kapasia', 'Kapasia'), ('Kaptai', 'Kaptai'), ('Karimganj', 'Karimganj'), ('Kasba', 'Kasba'), ('Kashiani', 'Kashiani'), ('Kathalia', 'Kathalia'), ('Katiadi', 'Katiadi'), ('Kaukhali', 'Kaukhali'), ('Kaukhali', 'Kaukhali'), ('Kaunia', 'Kaunia'), ('Kazipur', 'Kazipur'), ('Kendua Upazilla', 'Kendua Upazilla'), ('Keraniganj', 'Keraniganj'), ('Keshabpur', 'Keshabpur'), ('Khagrachhari', 'Khagrachhari'), ('Khaliajuri Upazilla', 'Khaliajuri Upazilla'), ('Khansama', 'Khansama'), ('Khetlal', 'Khetlal'), ('Khoksa', 'Khoksa'), ('Kishoreganj', 'Kishoreganj'), ('Kishoreganj Sadar', 'Kishoreganj Sadar'), ('Kobirhat', 'Kobirhat'), ('Komol Nagar', 'Komol Nagar'), ('Kotalipara', 'Kotalipara'), ('Kotchandpur', 'Kotchandpur'), ('Koyra', 'Koyra'), ('Kulaura', 'Kulaura'), ('Kuliarchar', 'Kuliarchar'), ('Kumarkhali', 'Kumarkhali'), ('Kurigram Sadar', 'Kurigram Sadar'), ('Kushtia Sadar', 'Kushtia Sadar'), ('Kutubdia', 'Kutubdia'), ('Lakhai', 'Lakhai'), ('Laksam', 'Laksam'), ('Lakshmichhari', 'Lakshmichhari'), ('Lakshmipur Sadar', 'Lakshmipur Sadar'), ('Lalmanirhat Sadar', 'Lalmanirhat Sadar'), ('Lalmohan', 'Lalmohan'), ('Lalpur', 'Lalpur'), ('Lama', 'Lama'), ('Langadu', 'Langadu'), ('Lohagara', 'Lohagara'), ('Lohagara Upazilla', 'Lohagara Upazilla'), ('Lohajang', 'Lohajang'), ('Madan Upazilla', 'Madan Upazilla'), ('Madarganj', 'Madarganj'), ('Madaripur Sadar', 'Madaripur Sadar'), ('Madhabpur', 'Madhabpur'), ('Madhukhali', 'Madhukhali'), ('Madhupur', 'Madhupur'), ('Magura Sadar', 'Magura Sadar'), ('Mahalchhari', 'Mahalchhari'), ('Maheshkhali', 'Maheshkhali'), ('Maheshpur', 'Maheshpur'), ('Manda', 'Manda'), ('Manikchhari', 'Manikchhari'), ('Manikganj Sadar', 'Manikganj Sadar'), ('Manirampur', 'Manirampur'), ('Manpura', 'Manpura'), ('Mathbaria', 'Mathbaria'), ('Matiranga', 'Matiranga'), ('Matlab Dakkhin', 'Matlab Dakkhin'), ('Matlab Uttar', 'Matlab Uttar'), ('Meghna', 'Meghna'), ('Mehendiganj', 'Mehendiganj'), ('Meherpur-S', 'Meherpur-S'), ('Melandaha', 'Melandaha'), ('Mirpur', 'Mirpur'), ('Mirsharai', 'Mirsharai'), ('Mirzaganj', 'Mirzaganj'), ('Mirzapur', 'Mirzapur'), ('Mithamain', 'Mithamain'), ('Mithapukur', 'Mithapukur'), ('Modhyanagar', 'Modhyanagar'), ('Mohadevpur', 'Mohadevpur'), ('Mohammadpur', 'Mohammadpur'), ('Mohanganj Upazilla', 'Mohanganj Upazilla'), ('Mohanpur', 'Mohanpur'), ('Mollahat', 'Mollahat'), ('Mongla', 'Mongla'), ('Monohardi', 'Monohardi'), ('Monohorgonj', 'Monohorgonj'), ('Morrelganj', 'Morrelganj'), ('Moulvibazar Sadar', 'Moulvibazar Sadar'), ('Mujib Nagar', 'Mujib Nagar'), ('Muksudpur', 'Muksudpur'), ('Muktagachha', 'Muktagachha'), ('Muladi', 'Muladi'), ('Munshiganj Sadar', 'Munshiganj Sadar'), ('Muradnagar', 'Muradnagar'), ('Mymensingh Sadar', 'Mymensingh Sadar'), ('Nabiganj', 'Nabiganj'), ('Nabinagar', 'Nabinagar'), ('Nachole', 'Nachole'), ('Nagarkanda', 'Nagarkanda'), ('Nagarpur', 'Nagarpur'), ('Nageshwari', 'Nageshwari'), ('Naikhongchhari', 'Naikhongchhari'), ('Nakla', 'Nakla'), ('Nalchity', 'Nalchity'), ('Nalitabari', 'Nalitabari'), ('Nandail', 'Nandail'), ('Nandigram', 'Nandigram'), ('Nangalkot', 'Nangalkot'), ('Nannerchar', 'Nannerchar'), ('Naogaon Sadar', 'Naogaon Sadar'), ('Narail-S Upazilla', 'Narail-S Upazilla'), ('Naria', 'Naria'), ('Narsingdi Sadar', 'Narsingdi Sadar'), ('Narundi Police I.C', 'Narundi Police I.C'), ('Naryanganj Sadar', 'Naryanganj Sadar'), ('Nasirnagar', 'Nasirnagar'), ('Natore Sadar', 'Natore Sadar'), ('Natore Sadar', 'Natore Sadar'), ('Nawabganj', 'Nawabganj'), ('Nawabganj', 'Nawabganj'), ('Nawabganj Sadar', 'Nawabganj Sadar'), ('Nazirpur', 'Nazirpur'), ('Nesarabad', 'Nesarabad'), ('Netrakona-S Upazilla', 'Netrakona-S Upazilla'), ('Niamatpur', 'Niamatpur'), ('Nikli', 'Nikli'), ('Nilphamari Sadar', 'Nilphamari Sadar'), ('Noakhali Sadar', 'Noakhali Sadar'), ('Nobigonj', 'Nobigonj'), ('Paba', 'Paba'), ('Pabna Sadar', 'Pabna Sadar'), ('Paikgachha', 'Paikgachha'), ('Pakundia', 'Pakundia'), ('Palash', 'Palash'), ('Palashbari', 'Palashbari'), ('Panchagarh Sadar', 'Panchagarh Sadar'), ('Panchbibi', 'Panchbibi'), ('Panchhari', 'Panchhari'), ('Pangsha', 'Pangsha'), ('Parbatipur', 'Parbatipur'), ('Parshuram', 'Parshuram'), ('Patgram', 'Patgram'), ('Patharghata', 'Patharghata'), ('Patiya', 'Patiya'), ('Patnitala', 'Patnitala'), ('Patuakhali Sadar', 'Patuakhali Sadar'), ('Pekua', 'Pekua'), ('Phulbari', 'Phulbari'), ('Phulbari', 'Phulbari'), ('Phulpur', 'Phulpur'), ('Phultala', 'Phultala'), ('Pirgachha', 'Pirgachha'), ('Pirganj', 'Pirganj'), ('Pirganj', 'Pirganj'), ('Pirojpur Sadar', 'Pirojpur Sadar'), ('Porsha', 'Porsha'), ('Purbadhala Upazilla', 'Purbadhala Upazilla'), ('Puthia', 'Puthia'), ('Raiganj', 'Raiganj'), ('Raipur', 'Raipur'), ('Raipura, Narsingdi', 'Raipura, Narsingdi'), ('Rajapur', 'Rajapur'), ('Rajarhat', 'Rajarhat'), ('Rajasthali', 'Rajasthali'), ('Rajbari Sadar', 'Rajbari Sadar'), ('Rajnagar', 'Rajnagar'), ('Rajoir', 'Rajoir'), ('Ramganj', 'Ramganj'), ('Ramgarh', 'Ramgarh'), ('Ramgati', 'Ramgati'), ('Rampal', 'Rampal'), ('Ramu', 'Ramu'), ('Rangabali', 'Rangabali'), ('Rangamati Sadar', 'Rangamati Sadar'), ('Rangpur Sadar', 'Rangpur Sadar'), ('Rangunia', 'Rangunia'), ('Raninagar', 'Raninagar'), ('Ranisankail', 'Ranisankail'), ('Raozan', 'Raozan'), ('Rowangchhari', 'Rowangchhari'), ('Rowmari', 'Rowmari'), ('Ruma', 'Ruma'), ('Rupganj', 'Rupganj'), ('Rupsa', 'Rupsa'), ('Sadarpur', 'Sadarpur'), ('Sadullapur', 'Sadullapur'), ('Saghata', 'Saghata'), ('Sahajanpur', 'Sahajanpur'), ('Saidpur', 'Saidpur'), ('Sakhipur', 'Sakhipur'), ('Sandwip', 'Sandwip'), ('Santhia', 'Santhia'), ('Sapahar', 'Sapahar'), ('Sarail', 'Sarail'), ('Sarankhola', 'Sarankhola'), ('Sariakandi', 'Sariakandi'), ('Sarishabari', 'Sarishabari'), ('Satkania', 'Satkania'), ('Satkhira Sadar', 'Satkhira Sadar'), ('Saturia', 'Saturia'), ('Savar', 'Savar'), ('Shahbazpur Town', 'Shahbazpur Town'), ('Shahjadpur', 'Shahjadpur'), ('Shahrasti', 'Shahrasti'), ('Shailkupa', 'Shailkupa'), ('Shaistagonj', 'Shaistagonj'), ('Shalikha', 'Shalikha'), ('Shaltha', 'Shaltha'), ('Shanthiganj', 'Shanthiganj'), ('Shariatpur Sadar -Palong', 'Shariatpur Sadar -Palong'), ('Sharsha', 'Sharsha'), ('Shenbag', 'Shenbag'), ('Sherpur', 'Sherpur'), ('Sherpur Sadar', 'Sherpur Sadar'), ('Shibalaya', 'Shibalaya'), ('Shibchar', 'Shibchar'), ('Shibganj', 'Shibganj'), ('Shibganj', 'Shibganj'), ('Shibpur', 'Shibpur'), ('Shyamnagar', 'Shyamnagar'), ('Siddirgonj', 'Siddirgonj'), ('Singair', 'Singair'), ('Sirajdikhan', 'Sirajdikhan'), ('Sirajganj Sadar', 'Sirajganj Sadar'), ('Sitakunda', 'Sitakunda'), ('Sonagazi', 'Sonagazi'), ('Sonaimuri', 'Sonaimuri'), ('Sonargaon', 'Sonargaon'), ('Sonatala', 'Sonatala'), ('Sreebardi', 'Sreebardi'), ('Sreemangal', 'Sreemangal'), ('Sreenagar', 'Sreenagar'), ('Sreepur', 'Sreepur'), ('Sripur', 'Sripur'), ('Suborno Char', 'Suborno Char'), ('Sujanagar', 'Sujanagar'), ('Sulla', 'Sulla'), ('Sunamganj Sadar', 'Sunamganj Sadar'), ('Sundarganj', 'Sundarganj'), ('Sylhet Sadar', 'Sylhet Sadar'), ('Tahirpur', 'Tahirpur'), ('Tala', 'Tala'), ('Taltali', 'Taltali'), ('Tangail Sadar', 'Tangail Sadar'), ('Tanore', 'Tanore'), ('Taraganj', 'Taraganj'), ('Tarail', 'Tarail'), ('Tarash', 'Tarash'), ('Tazumuddin', 'Tazumuddin'), ('Teknaf', 'Teknaf'), ('Terokhada', 'Terokhada'), ('Tetulia', 'Tetulia'), ('Thakurgaon Sadar', 'Thakurgaon Sadar'), ('Thanchi', 'Thanchi'), ('Titas', 'Titas'), ('Tongi', 'Tongi'), ('Tongibari', 'Tongibari'), ('Trishal', 'Trishal'), ('Tungipara', 'Tungipara'), ('Ukhia', 'Ukhia'), ('Ulipur', 'Ulipur'), ('Ullahpara', 'Ullahpara'), ('Wazirpur', 'Wazirpur'), ('Zakiganj', 'Zakiganj'), ('Zianagar', 'Zianagar'), ('angni', 'angni'), ("{{198}}''{{199}}", "{{198}}''{{199}}")], max_length=255, null=True),
        ),
    ]
