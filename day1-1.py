Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

===== RESTART: C:/Users/Laptop/OneDrive/Documents/stfc/openreadprintfile.py ====
Traceback (most recent call last):
  File "C:/Users/Laptop/OneDrive/Documents/stfc/openreadprintfile.py", line 7, in <module>
    file1 = open('2022-06-01-2019__ccsrm.in2p3.fr__mover.pp.rl.ac', 'r')
FileNotFoundError: [Errno 2] No such file or directory: '2022-06-01-2019__ccsrm.in2p3.fr__mover.pp.rl.ac'

===== RESTART: C:/Users/Laptop/OneDrive/Documents/stfc/openreadprintfile.py ====
Traceback (most recent call last):
  File "C:/Users/Laptop/OneDrive/Documents/stfc/openreadprintfile.py", line 7, in <module>
    file1 = open('testfile.txt', 'r')
FileNotFoundError: [Errno 2] No such file or directory: 'testfile.txt'

===== RESTART: C:/Users/Laptop/OneDrive/Documents/stfc/openreadprintfile.py ====
Traceback (most recent call last):
  File "C:/Users/Laptop/OneDrive/Documents/stfc/openreadprintfile.py", line 6, in <module>
    file1 = open('testfile.txt', 'r')
FileNotFoundError: [Errno 2] No such file or directory: 'testfile.txt'

===== RESTART: C:/Users/Laptop/OneDrive/Documents/stfc/openreadprintfile.py ====
Traceback (most recent call last):
  File "C:/Users/Laptop/OneDrive/Documents/stfc/openreadprintfile.py", line 5, in <module>
    file1 = open('testfile', 'r')
FileNotFoundError: [Errno 2] No such file or directory: 'testfile'

===== RESTART: C:/Users/Laptop/OneDrive/Documents/stfc/openreadprintfile.py ====
Traceback (most recent call last):
  File "C:/Users/Laptop/OneDrive/Documents/stfc/openreadprintfile.py", line 5, in <module>
    file1 = open('C:/Users/Laptop/OneDrive/Documents/stfc/testfile.txt', 'r')
FileNotFoundError: [Errno 2] No such file or directory: 'C:/Users/Laptop/OneDrive/Documents/stfc/testfile.txt'

===== RESTART: C:/Users/Laptop/OneDrive/Documents/stfc/openreadprintfile.py ====
Traceback (most recent call last):
  File "C:/Users/Laptop/OneDrive/Documents/stfc/openreadprintfile.py", line 5, in <module>
    file1 = open('C:/Users/Laptop/OneDrive/Documents/stfc/testfile', 'r')
FileNotFoundError: [Errno 2] No such file or directory: 'C:/Users/Laptop/OneDrive/Documents/stfc/testfile'
import os
os.listdir()
['openreadprintfile.py', 'testfile.uk__2112722584__17762e5e-e1e8-11ec-a73d-001dd8b71d1a']

========================================================= RESTART: C:/Users/Laptop/OneDrive/Documents/stfc/openreadprintfile.py ========================================================
Line1: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Transfer accepted
Line2: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Proxy: /tmp/x509up_h4433923159900929368XdcXchXdcXcernXouXorganicXunitsXouXusersXcnXcmsrucioXcnX779320XcnXrobotXXcmsXrucioXdataXtransfer
Line3: INFO    Wed, 01 Jun 2022 21:19:09 +0100; VO: cms
Line4: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Job id: 17762e5e-e1e8-11ec-a73d-001dd8b71d1a
Line5: INFO    Wed, 01 Jun 2022 21:19:09 +0100; File id: 2112722584
Line6: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Source url: srm://ccsrm.in2p3.fr:8443/srm/managerv2?SFN=/pnfs/in2p3.fr/data/cms/disk/data/store/test/loadtest/source/T1_FR_CCIN2P3_Disk/urandom.270MB.file0000
Line7: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Dest url: gsiftp://mover.pp.rl.ac.uk:2811/pnfs/pp.rl.ac.uk/data/cms/store/test/loadtest/source/T1_FR_CCIN2P3_Disk/urandom.270MB.file0000
Line8: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Overwrite enabled: 1
Line9: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Disable delegation: 0
Line10: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Disable local streaming: 0
Line11: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Dest space token:
Line12: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Source space token:
Line13: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Checksum: 548de7b7
Line14: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Checksum enabled: Both checksum comparison
Line15: INFO    Wed, 01 Jun 2022 21:19:09 +0100; User filesize: 270000000
Line16: INFO    Wed, 01 Jun 2022 21:19:09 +0100; File metadata: {\"dst_type\":?\"DISK\",?\"name\":?\"/store/test/loadtest/source/T1_FR_CCIN2P3_Disk/urandom.270MB.file0000\",?\"adler32\":?\"548de7b7\",?\"src_rse\":?\"T1_FR_CCIN2P3_Disk\",?\"activity\":?\"Functional?Test\",?\"src_rse_id\":?\"112105749e764d9b8df8f6ca866e4ef8\",?\"request_id\":?\"07ff2b749b7248aba2a907d4315584fd\",?\"request_type\":?\"TRANSFER\",?\"filesize\":?270000000,?\"dest_rse_id\":?\"20f028e6e514453e88f7f2894e86b0ef\",?\"scope\":?\"cms\",?\"dst_rse\":?\"T2_UK_SGrid_RALPP\",?\"src_type\":?\"DISK\",?\"md5\":?\"07d43f0e4ffe60757615eead1c9ea7e0\"}
Line17: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Job metadata: {\"auth_method\":?\"certificate\",?\"multi_sources\":?false,?\"issuer\":?\"rucio\"}
Line18: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Bringonline token:
Line19: INFO    Wed, 01 Jun 2022 21:19:09 +0100; UDT: 0
Line20: INFO    Wed, 01 Jun 2022 21:19:09 +0100; BDII:lcgbdii.gridpp.rl.ac.uk:2170
Line21: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Source token issuer:
Line22: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Destination token issuer:
Line23: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Report on the destination tape file: 0
Line24: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Getting source file size
Line25: INFO    Wed, 01 Jun 2022 21:19:09 +0100; File size: 270000000
Line26: INFO    Wed, 01 Jun 2022 21:19:09 +0100; IPv6: indeterminate
Line27: INFO    Wed, 01 Jun 2022 21:19:09 +0100; TCP streams: 0
Line28: INFO    Wed, 01 Jun 2022 21:19:09 +0100; TCP buffer size: 0
Line29: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Timeout set to: 1115
Line30: INFO    Wed, 01 Jun 2022 21:19:09 +0100; [1654114749635] BOTH GFAL2:CORE:COPY	LIST:ENTER
Line31: INFO    Wed, 01 Jun 2022 21:19:09 +0100; [1654114749635] BOTH GFAL2:CORE:COPY	LIST:ITEM	srm://ccsrm.in2p3.fr:8443/srm/managerv2?SFN=/pnfs/in2p3.fr/data/cms/disk/data/store/test/loadtest/source/T1_FR_CCIN2P3_Disk/urandom.270MB.file0000 => gsiftp://mover.pp.rl.ac.uk:2811/pnfs/pp.rl.ac.uk/data/cms/store/test/loadtest/source/T1_FR_CCIN2P3_Disk/urandom.270MB.file0000
Line32: INFO    Wed, 01 Jun 2022 21:19:09 +0100; [1654114749635] BOTH GFAL2:CORE:COPY	LIST:EXIT
Line33: INFO    Wed, 01 Jun 2022 21:19:09 +0100; [1654114749656] BOTH SRM	PREPARE:ENTER
Line34: INFO    Wed, 01 Jun 2022 21:19:09 +0100; [1654114749656] SOURCE SRM	CHECKSUM:ENTER
Line35: INFO    Wed, 01 Jun 2022 21:19:09 +0100; [1654114749697] SOURCE SRM	CHECKSUM:EXIT
Line36: INFO    Wed, 01 Jun 2022 21:19:09 +0100; [1654114749755] SOURCE GFAL2::PLUGINS::SRM	SRM:GET	Got TURL srm://ccsrm.in2p3.fr:8443/srm/managerv2?SFN=/pnfs/in2p3.fr/data/cms/disk/data/store/test/loadtest/source/T1_FR_CCIN2P3_Disk/urandom.270MB.file0000 => gsiftp://ccdcatli308.in2p3.fr:2811//pnfs/in2p3.fr/data/cms/disk/data/store/test/loadtest/source/T1_FR_CCIN2P3_Disk/urandom.270MB.file0000
Line37: INFO    Wed, 01 Jun 2022 21:19:09 +0100; [1654114749755] BOTH SRM	PREPARE:EXIT
Line38: INFO    Wed, 01 Jun 2022 21:19:09 +0100; [1654114749755] BOTH GFAL2:CORE:COPY	LIST:ENTER
Line39: INFO    Wed, 01 Jun 2022 21:19:09 +0100; [1654114749755] BOTH GFAL2:CORE:COPY	LIST:ITEM	gsiftp://ccdcatli308.in2p3.fr:2811//pnfs/in2p3.fr/data/cms/disk/data/store/test/loadtest/source/T1_FR_CCIN2P3_Disk/urandom.270MB.file0000 => gsiftp://mover.pp.rl.ac.uk:2811/pnfs/pp.rl.ac.uk/data/cms/store/test/loadtest/source/T1_FR_CCIN2P3_Disk/urandom.270MB.file0000
Line40: INFO    Wed, 01 Jun 2022 21:19:09 +0100; [1654114749755] BOTH GFAL2:CORE:COPY	LIST:EXIT
Line41: INFO    Wed, 01 Jun 2022 21:19:09 +0100; [1654114749773] BOTH GSIFTP	TRANSFER:ENTER	([2001:660:5009:9:193:48:99:128]:2811) gsiftp://ccdcatli308.in2p3.fr:2811//pnfs/in2p3.fr/data/cms/disk/data/store/test/loadtest/source/T1_FR_CCIN2P3_Disk/urandom.270MB.file0000 => ([2001:630:58:1c20::82f6:2fea]:2811) gsiftp://mover.pp.rl.ac.uk:2811/pnfs/pp.rl.ac.uk/data/cms/store/test/loadtest/source/T1_FR_CCIN2P3_Disk/urandom.270MB.file0000
Line42: INFO    Wed, 01 Jun 2022 21:19:09 +0100; [1654114749773] BOTH GSIFTP	TRANSFER:TYPE	3rd push
Line43: INFO    Wed, 01 Jun 2022 21:19:09 +0100; [1654114749873] DEST GSIFTP	OVERWRITE	Deleted gsiftp://mover.pp.rl.ac.uk:2811/pnfs/pp.rl.ac.uk/data/cms/store/test/loadtest/source/T1_FR_CCIN2P3_Disk/urandom.270MB.file0000
Line44: INFO    Wed, 01 Jun 2022 21:19:10 +0100; [1654114750436] DEST GSIFTP	PASV	mover.pp.rl.ac.uk:[2001:630:58:1c20::82f6:2faa]:50190
Line45: INFO    Wed, 01 Jun 2022 21:19:10 +0100; [1654114750436] DEST GSIFTP	IPv6	[2001:630:58:1c20::82f6:2faa]:50190
Line46: INFO    Wed, 01 Jun 2022 21:19:13 +0100; bytes: 270000000, avg KB/sec:90921, inst KB/sec:90921, elapsed:3
Line47: INFO    Wed, 01 Jun 2022 21:19:13 +0100; [1654114753333] BOTH GSIFTP	TRANSFER:EXIT	([2001:660:5009:9:193:48:99:128]:2811) gsiftp://ccdcatli308.in2p3.fr:2811//pnfs/in2p3.fr/data/cms/disk/data/store/test/loadtest/source/T1_FR_CCIN2P3_Disk/urandom.270MB.file0000 => ([2001:630:58:1c20::82f6:2fea]:2811) gsiftp://mover.pp.rl.ac.uk:2811/pnfs/pp.rl.ac.uk/data/cms/store/test/loadtest/source/T1_FR_CCIN2P3_Disk/urandom.270MB.file0000
Line48: INFO    Wed, 01 Jun 2022 21:19:13 +0100; [1654114753333] DEST SRM	CLOSE:ENTER	gsiftp://mover.pp.rl.ac.uk:2811/pnfs/pp.rl.ac.uk/data/cms/store/test/loadtest/source/T1_FR_CCIN2P3_Disk/urandom.270MB.file0000
Line49: INFO    Wed, 01 Jun 2022 21:19:13 +0100; [1654114753333] DEST SRM	CLOSE:EXIT	gsiftp://mover.pp.rl.ac.uk:2811/pnfs/pp.rl.ac.uk/data/cms/store/test/loadtest/source/T1_FR_CCIN2P3_Disk/urandom.270MB.file0000
Line50: INFO    Wed, 01 Jun 2022 21:19:13 +0100; [1654114753333] DEST SRM	CHECKSUM:ENTER
Line51: INFO    Wed, 01 Jun 2022 21:19:13 +0100; [1654114753468] DEST SRM	CHECKSUM:EXIT
Line52: INFO    Wed, 01 Jun 2022 21:19:13 +0100; DESTINATION Source and destination file size matching
Line53: WARNING Wed, 01 Jun 2022 21:19:13 +0100; Timeout stopped
Line54: INFO    Wed, 01 Jun 2022 21:19:13 +0100; Transfer finished successfully

========================================================= RESTART: C:/Users/Laptop/OneDrive/Documents/stfc/openreadprintfile.py ========================================================
Line1: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Transfer accepted

========================================================= RESTART: C:/Users/Laptop/OneDrive/Documents/stfc/openreadprintfile.py ========================================================
Line1: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Transfer accepted

========================================================= RESTART: C:/Users/Laptop/OneDrive/Documents/stfc/openreadprintfile.py ========================================================
Line1: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Transfer accepted
Line2: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Proxy: /tmp/x509up_h4433923159900929368XdcXchXdcXcernXouXorganicXunitsXouXusersXcnXcmsrucioXcnX779320XcnXrobotXXcmsXrucioXdataXtransfer
Line3: INFO    Wed, 01 Jun 2022 21:19:09 +0100; VO: cms
Line4: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Job id: 17762e5e-e1e8-11ec-a73d-001dd8b71d1a
Line5: INFO    Wed, 01 Jun 2022 21:19:09 +0100; File id: 2112722584
Line6: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Source url: srm://ccsrm.in2p3.fr:8443/srm/managerv2?SFN=/pnfs/in2p3.fr/data/cms/disk/data/store/test/loadtest/source/T1_FR_CCIN2P3_Disk/urandom.270MB.file0000
Line7: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Dest url: gsiftp://mover.pp.rl.ac.uk:2811/pnfs/pp.rl.ac.uk/data/cms/store/test/loadtest/source/T1_FR_CCIN2P3_Disk/urandom.270MB.file0000
Line8: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Overwrite enabled: 1
Line9: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Disable delegation: 0
Line10: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Disable local streaming: 0
Line11: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Dest space token:
Line12: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Source space token:
Line13: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Checksum: 548de7b7
Line14: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Checksum enabled: Both checksum comparison
Line15: INFO    Wed, 01 Jun 2022 21:19:09 +0100; User filesize: 270000000
Line16: INFO    Wed, 01 Jun 2022 21:19:09 +0100; File metadata: {\"dst_type\":?\"DISK\",?\"name\":?\"/store/test/loadtest/source/T1_FR_CCIN2P3_Disk/urandom.270MB.file0000\",?\"adler32\":?\"548de7b7\",?\"src_rse\":?\"T1_FR_CCIN2P3_Disk\",?\"activity\":?\"Functional?Test\",?\"src_rse_id\":?\"112105749e764d9b8df8f6ca866e4ef8\",?\"request_id\":?\"07ff2b749b7248aba2a907d4315584fd\",?\"request_type\":?\"TRANSFER\",?\"filesize\":?270000000,?\"dest_rse_id\":?\"20f028e6e514453e88f7f2894e86b0ef\",?\"scope\":?\"cms\",?\"dst_rse\":?\"T2_UK_SGrid_RALPP\",?\"src_type\":?\"DISK\",?\"md5\":?\"07d43f0e4ffe60757615eead1c9ea7e0\"}
Line17: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Job metadata: {\"auth_method\":?\"certificate\",?\"multi_sources\":?false,?\"issuer\":?\"rucio\"}
Line18: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Bringonline token:
Line19: INFO    Wed, 01 Jun 2022 21:19:09 +0100; UDT: 0
Line20: INFO    Wed, 01 Jun 2022 21:19:09 +0100; BDII:lcgbdii.gridpp.rl.ac.uk:2170
Line21: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Source token issuer:
Line22: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Destination token issuer:
Line23: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Report on the destination tape file: 0
Line24: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Getting source file size
Line25: INFO    Wed, 01 Jun 2022 21:19:09 +0100; File size: 270000000
Line26: INFO    Wed, 01 Jun 2022 21:19:09 +0100; IPv6: indeterminate
Line27: INFO    Wed, 01 Jun 2022 21:19:09 +0100; TCP streams: 0
Line28: INFO    Wed, 01 Jun 2022 21:19:09 +0100; TCP buffer size: 0
Line29: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Timeout set to: 1115
Line30: INFO    Wed, 01 Jun 2022 21:19:09 +0100; [1654114749635] BOTH GFAL2:CORE:COPY	LIST:ENTER
Line31: INFO    Wed, 01 Jun 2022 21:19:09 +0100; [1654114749635] BOTH GFAL2:CORE:COPY	LIST:ITEM	srm://ccsrm.in2p3.fr:8443/srm/managerv2?SFN=/pnfs/in2p3.fr/data/cms/disk/data/store/test/loadtest/source/T1_FR_CCIN2P3_Disk/urandom.270MB.file0000 => gsiftp://mover.pp.rl.ac.uk:2811/pnfs/pp.rl.ac.uk/data/cms/store/test/loadtest/source/T1_FR_CCIN2P3_Disk/urandom.270MB.file0000
Line32: INFO    Wed, 01 Jun 2022 21:19:09 +0100; [1654114749635] BOTH GFAL2:CORE:COPY	LIST:EXIT
Line33: INFO    Wed, 01 Jun 2022 21:19:09 +0100; [1654114749656] BOTH SRM	PREPARE:ENTER
Line34: INFO    Wed, 01 Jun 2022 21:19:09 +0100; [1654114749656] SOURCE SRM	CHECKSUM:ENTER
Line35: INFO    Wed, 01 Jun 2022 21:19:09 +0100; [1654114749697] SOURCE SRM	CHECKSUM:EXIT
Line36: INFO    Wed, 01 Jun 2022 21:19:09 +0100; [1654114749755] SOURCE GFAL2::PLUGINS::SRM	SRM:GET	Got TURL srm://ccsrm.in2p3.fr:8443/srm/managerv2?SFN=/pnfs/in2p3.fr/data/cms/disk/data/store/test/loadtest/source/T1_FR_CCIN2P3_Disk/urandom.270MB.file0000 => gsiftp://ccdcatli308.in2p3.fr:2811//pnfs/in2p3.fr/data/cms/disk/data/store/test/loadtest/source/T1_FR_CCIN2P3_Disk/urandom.270MB.file0000
Line37: INFO    Wed, 01 Jun 2022 21:19:09 +0100; [1654114749755] BOTH SRM	PREPARE:EXIT
Line38: INFO    Wed, 01 Jun 2022 21:19:09 +0100; [1654114749755] BOTH GFAL2:CORE:COPY	LIST:ENTER
Line39: INFO    Wed, 01 Jun 2022 21:19:09 +0100; [1654114749755] BOTH GFAL2:CORE:COPY	LIST:ITEM	gsiftp://ccdcatli308.in2p3.fr:2811//pnfs/in2p3.fr/data/cms/disk/data/store/test/loadtest/source/T1_FR_CCIN2P3_Disk/urandom.270MB.file0000 => gsiftp://mover.pp.rl.ac.uk:2811/pnfs/pp.rl.ac.uk/data/cms/store/test/loadtest/source/T1_FR_CCIN2P3_Disk/urandom.270MB.file0000
Line40: INFO    Wed, 01 Jun 2022 21:19:09 +0100; [1654114749755] BOTH GFAL2:CORE:COPY	LIST:EXIT
Line41: INFO    Wed, 01 Jun 2022 21:19:09 +0100; [1654114749773] BOTH GSIFTP	TRANSFER:ENTER	([2001:660:5009:9:193:48:99:128]:2811) gsiftp://ccdcatli308.in2p3.fr:2811//pnfs/in2p3.fr/data/cms/disk/data/store/test/loadtest/source/T1_FR_CCIN2P3_Disk/urandom.270MB.file0000 => ([2001:630:58:1c20::82f6:2fea]:2811) gsiftp://mover.pp.rl.ac.uk:2811/pnfs/pp.rl.ac.uk/data/cms/store/test/loadtest/source/T1_FR_CCIN2P3_Disk/urandom.270MB.file0000
Line42: INFO    Wed, 01 Jun 2022 21:19:09 +0100; [1654114749773] BOTH GSIFTP	TRANSFER:TYPE	3rd push
Line43: INFO    Wed, 01 Jun 2022 21:19:09 +0100; [1654114749873] DEST GSIFTP	OVERWRITE	Deleted gsiftp://mover.pp.rl.ac.uk:2811/pnfs/pp.rl.ac.uk/data/cms/store/test/loadtest/source/T1_FR_CCIN2P3_Disk/urandom.270MB.file0000
Line44: INFO    Wed, 01 Jun 2022 21:19:10 +0100; [1654114750436] DEST GSIFTP	PASV	mover.pp.rl.ac.uk:[2001:630:58:1c20::82f6:2faa]:50190
Line45: INFO    Wed, 01 Jun 2022 21:19:10 +0100; [1654114750436] DEST GSIFTP	IPv6	[2001:630:58:1c20::82f6:2faa]:50190
Line46: INFO    Wed, 01 Jun 2022 21:19:13 +0100; bytes: 270000000, avg KB/sec:90921, inst KB/sec:90921, elapsed:3
Line47: INFO    Wed, 01 Jun 2022 21:19:13 +0100; [1654114753333] BOTH GSIFTP	TRANSFER:EXIT	([2001:660:5009:9:193:48:99:128]:2811) gsiftp://ccdcatli308.in2p3.fr:2811//pnfs/in2p3.fr/data/cms/disk/data/store/test/loadtest/source/T1_FR_CCIN2P3_Disk/urandom.270MB.file0000 => ([2001:630:58:1c20::82f6:2fea]:2811) gsiftp://mover.pp.rl.ac.uk:2811/pnfs/pp.rl.ac.uk/data/cms/store/test/loadtest/source/T1_FR_CCIN2P3_Disk/urandom.270MB.file0000
Line48: INFO    Wed, 01 Jun 2022 21:19:13 +0100; [1654114753333] DEST SRM	CLOSE:ENTER	gsiftp://mover.pp.rl.ac.uk:2811/pnfs/pp.rl.ac.uk/data/cms/store/test/loadtest/source/T1_FR_CCIN2P3_Disk/urandom.270MB.file0000
Line49: INFO    Wed, 01 Jun 2022 21:19:13 +0100; [1654114753333] DEST SRM	CLOSE:EXIT	gsiftp://mover.pp.rl.ac.uk:2811/pnfs/pp.rl.ac.uk/data/cms/store/test/loadtest/source/T1_FR_CCIN2P3_Disk/urandom.270MB.file0000
Line50: INFO    Wed, 01 Jun 2022 21:19:13 +0100; [1654114753333] DEST SRM	CHECKSUM:ENTER
Line51: INFO    Wed, 01 Jun 2022 21:19:13 +0100; [1654114753468] DEST SRM	CHECKSUM:EXIT
Line52: INFO    Wed, 01 Jun 2022 21:19:13 +0100; DESTINATION Source and destination file size matching
Line53: WARNING Wed, 01 Jun 2022 21:19:13 +0100; Timeout stopped
Line54: INFO    Wed, 01 Jun 2022 21:19:13 +0100; Transfer finished successfully

========================================================= RESTART: C:/Users/Laptop/OneDrive/Documents/stfc/openreadprintfile.py ========================================================
Line1: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Transfer accepted

========================================================= RESTART: C:/Users/Laptop/OneDrive/Documents/stfc/openreadprintfile.py ========================================================

========================================================= RESTART: C:/Users/Laptop/OneDrive/Documents/stfc/openreadprintfile.py ========================================================
['INFO    Wed, 01 Jun 2022 21:19:09 +0100; Transfer accepted\n']

========= RESTART: C:/Users/Laptop/OneDrive/Documents/stfc/openreadprintfile.py ========

========= RESTART: C:/Users/Laptop/OneDrive/Documents/stfc/openreadprintfile.py ========
Line2: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Proxy: /tmp/x509up_h4433923159900929368XdcXchXdcXcernXouXorganicXunitsXouXusersXcnXcmsrucioXcnX779320XcnXrobotXXcmsXrucioXdataXtransfer

========= RESTART: C:/Users/Laptop/OneDrive/Documents/stfc/openreadprintfile.py ========
Line3: INFO    Wed, 01 Jun 2022 21:19:09 +0100; VO: cms

========= RESTART: C:/Users/Laptop/OneDrive/Documents/stfc/openreadprintfile.py ========
Line3: INFO    Wed, 01 Jun 2022 21:19:09 +0100; VO: cms
Line15: INFO    Wed, 01 Jun 2022 21:19:09 +0100; User filesize: 270000000

========= RESTART: C:/Users/Laptop/OneDrive/Documents/stfc/openreadprintfile.py ========
Line3: INFO    Wed, 01 Jun 2022 21:19:09 +0100; VO: cms
Line15: INFO    Wed, 01 Jun 2022 21:19:09 +0100; User filesize: 270000000
Traceback (most recent call last):
  File "C:/Users/Laptop/OneDrive/Documents/stfc/openreadprintfile.py", line 18, in <module>
    linefind(VO)
NameError: name 'linefind' is not defined

========= RESTART: C:/Users/Laptop/OneDrive/Documents/stfc/openreadprintfile.py ========
Line3: INFO    Wed, 01 Jun 2022 21:19:09 +0100; VO: cms
Line15: INFO    Wed, 01 Jun 2022 21:19:09 +0100; User filesize: 270000000
Traceback (most recent call last):
  File "C:/Users/Laptop/OneDrive/Documents/stfc/openreadprintfile.py", line 18, in <module>
    findline(VO)
NameError: name 'findline' is not defined

========= RESTART: C:/Users/Laptop/OneDrive/Documents/stfc/openreadprintfile.py ========
Line3: INFO    Wed, 01 Jun 2022 21:19:09 +0100; VO: cms
Line15: INFO    Wed, 01 Jun 2022 21:19:09 +0100; User filesize: 270000000
Traceback (most recent call last):
  File "C:/Users/Laptop/OneDrive/Documents/stfc/openreadprintfile.py", line 18, in <module>
    locate(VO)
NameError: name 'locate' is not defined. Did you mean: 'locals'?

========= RESTART: C:/Users/Laptop/OneDrive/Documents/stfc/openreadprintfile.py ========
Line3: INFO    Wed, 01 Jun 2022 21:19:09 +0100; VO: cms
Line15: INFO    Wed, 01 Jun 2022 21:19:09 +0100; User filesize: 270000000
Traceback (most recent call last):
  File "C:/Users/Laptop/OneDrive/Documents/stfc/openreadprintfile.py", line 18, in <module>
    for line in file:
NameError: name 'file' is not defined. Did you mean: 'file1'?

========= RESTART: C:/Users/Laptop/OneDrive/Documents/stfc/openreadprintfile.py ========
Line3: INFO    Wed, 01 Jun 2022 21:19:09 +0100; VO: cms
Line15: INFO    Wed, 01 Jun 2022 21:19:09 +0100; User filesize: 270000000
Traceback (most recent call last):
  File "C:/Users/Laptop/OneDrive/Documents/stfc/openreadprintfile.py", line 24, in <module>
    print(linenum-1)
NameError: name 'linenum' is not defined

========= RESTART: C:/Users/Laptop/OneDrive/Documents/stfc/openreadprintfile.py ========
Line3: INFO    Wed, 01 Jun 2022 21:19:09 +0100; VO: cms
Line15: INFO    Wed, 01 Jun 2022 21:19:09 +0100; User filesize: 270000000
-1
enter the word you want us to count, and will tell you on which lineVO
Traceback (most recent call last):
  File "C:/Users/Laptop/OneDrive/Documents/stfc/openreadprintfile.py", line 31, in <module>
    with open(name, 'r') as inF:
NameError: name 'name' is not defined

========= RESTART: C:/Users/Laptop/OneDrive/Documents/stfc/openreadprintfile.py ========
Line3: INFO    Wed, 01 Jun 2022 21:19:09 +0100; VO: cms
Line15: INFO    Wed, 01 Jun 2022 21:19:09 +0100; User filesize: 270000000
-1
enter the word you want us to count, and will tell you on which lineVO
Traceback (most recent call last):
  File "C:/Users/Laptop/OneDrive/Documents/stfc/openreadprintfile.py", line 31, in <module>
    with open(word, 'r') as inF:
FileNotFoundError: [Errno 2] No such file or directory: 'VO'

========= RESTART: C:/Users/Laptop/OneDrive/Documents/stfc/openreadprintfile.py ========
Line3: INFO    Wed, 01 Jun 2022 21:19:09 +0100; VO: cms
Line15: INFO    Wed, 01 Jun 2022 21:19:09 +0100; User filesize: 270000000
-1
enter the word you want us to count, and will tell you on which lineVO
Traceback (most recent call last):
  File "C:/Users/Laptop/OneDrive/Documents/stfc/openreadprintfile.py", line 31, in <module>
    with open(file1, 'r') as inF:
TypeError: expected str, bytes or os.PathLike object, not TextIOWrapper

========= RESTART: C:/Users/Laptop/OneDrive/Documents/stfc/openreadprintfile.py ========
Line3: INFO    Wed, 01 Jun 2022 21:19:09 +0100; VO: cms
Line15: INFO    Wed, 01 Jun 2022 21:19:09 +0100; User filesize: 270000000
-1
enter the word you want us to count, and will tell you on which lineVO

========= RESTART: C:/Users/Laptop/OneDrive/Documents/stfc/openreadprintfile.py ========
Line3: INFO    Wed, 01 Jun 2022 21:19:09 +0100; VO: cms
Line15: INFO    Wed, 01 Jun 2022 21:19:09 +0100; User filesize: 270000000
-1
enter the word you want us to count, and will tell you on which lineVO
<_io.TextIOWrapper name='testfile.uk__2112722584__17762e5e-e1e8-11ec-a73d-001dd8b71d1a' mode='r' encoding='cp1252'>

========= RESTART: C:/Users/Laptop/OneDrive/Documents/stfc/openreadprintfile.py ========
Line3: INFO    Wed, 01 Jun 2022 21:19:09 +0100; VO: cms
Line15: INFO    Wed, 01 Jun 2022 21:19:09 +0100; User filesize: 270000000
-1
enter the word you want us to count, and will tell you on which lineVO
INFO    Wed, 01 Jun 2022 21:19:13 +0100; Transfer finished successfully


========= RESTART: C:/Users/Laptop/OneDrive/Documents/stfc/openreadprintfile.py ========
Line3: INFO    Wed, 01 Jun 2022 21:19:09 +0100; VO: cms
Line15: INFO    Wed, 01 Jun 2022 21:19:09 +0100; User filesize: 270000000
found at line: 3

========= RESTART: C:/Users/Laptop/OneDrive/Documents/stfc/openreadprintfile.py ========
line: 3
line: 15
Line54: INFO    Wed, 01 Jun 2022 21:19:13 +0100; Transfer finished successfully
Line54: INFO    Wed, 01 Jun 2022 21:19:13 +0100; Transfer finished successfully

========= RESTART: C:/Users/Laptop/OneDrive/Documents/stfc/openreadprintfile.py ========
line: 3
line: 15

========= RESTART: C:/Users/Laptop/OneDrive/Documents/stfc/openreadprintfile.py ========
line: 3
line: 15
Line54: INFO    Wed, 01 Jun 2022 21:19:13 +0100; Transfer finished successfully
Line54: INFO    Wed, 01 Jun 2022 21:19:13 +0100; Transfer finished successfully

========= RESTART: C:/Users/Laptop/OneDrive/Documents/stfc/openreadprintfile.py ========
line: 3
line: 15
Line3: INFO    Wed, 01 Jun 2022 21:19:13 +0100; Transfer finished successfully
Line15: INFO    Wed, 01 Jun 2022 21:19:13 +0100; Transfer finished successfully

========= RESTART: C:/Users/Laptop/OneDrive/Documents/stfc/openreadprintfile.py ========
line: 3
line: 15
Line54: INFO    Wed, 01 Jun 2022 21:19:13 +0100; Transfer finished successfully
Line54: INFO    Wed, 01 Jun 2022 21:19:13 +0100; Transfer finished successfully

========= RESTART: C:/Users/Laptop/OneDrive/Documents/stfc/openreadprintfile.py ========
line: 3
line: 15
Line3: INFO    Wed, 01 Jun 2022 21:19:09 +0100; VO: cms
Line15: INFO    Wed, 01 Jun 2022 21:19:09 +0100; User filesize: 270000000

========= RESTART: C:/Users/Laptop/OneDrive/Documents/stfc/openreadprintfile.py ========
line: 3
line: 15
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Transfer accepted
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Transfer accepted
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Proxy: /tmp/x509up_h4433923159900929368XdcXchXdcXcernXouXorganicXunitsXouXusersXcnXcmsrucioXcnX779320XcnXrobotXXcmsXrucioXdataXtransfer
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Proxy: /tmp/x509up_h4433923159900929368XdcXchXdcXcernXouXorganicXunitsXouXusersXcnXcmsrucioXcnX779320XcnXrobotXXcmsXrucioXdataXtransfer
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; VO: cms
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; VO: cms
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Job id: 17762e5e-e1e8-11ec-a73d-001dd8b71d1a
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Job id: 17762e5e-e1e8-11ec-a73d-001dd8b71d1a
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; File id: 2112722584
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; File id: 2112722584
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Source url: srm://ccsrm.in2p3.fr:8443/srm/managerv2?SFN=/pnfs/in2p3.fr/data/cms/disk/data/store/test/loadtest/source/T1_FR_CCIN2P3_Disk/urandom.270MB.file0000
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Source url: srm://ccsrm.in2p3.fr:8443/srm/managerv2?SFN=/pnfs/in2p3.fr/data/cms/disk/data/store/test/loadtest/source/T1_FR_CCIN2P3_Disk/urandom.270MB.file0000
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Dest url: gsiftp://mover.pp.rl.ac.uk:2811/pnfs/pp.rl.ac.uk/data/cms/store/test/loadtest/source/T1_FR_CCIN2P3_Disk/urandom.270MB.file0000
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Dest url: gsiftp://mover.pp.rl.ac.uk:2811/pnfs/pp.rl.ac.uk/data/cms/store/test/loadtest/source/T1_FR_CCIN2P3_Disk/urandom.270MB.file0000
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Overwrite enabled: 1
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Overwrite enabled: 1
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Disable delegation: 0
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Disable delegation: 0
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Disable local streaming: 0
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Disable local streaming: 0
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Dest space token:
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Dest space token:
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Source space token:
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Source space token:
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Checksum: 548de7b7
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Checksum: 548de7b7
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Checksum enabled: Both checksum comparison
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Checksum enabled: Both checksum comparison
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; User filesize: 270000000
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; User filesize: 270000000
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; File metadata: {\"dst_type\":?\"DISK\",?\"name\":?\"/store/test/loadtest/source/T1_FR_CCIN2P3_Disk/urandom.270MB.file0000\",?\"adler32\":?\"548de7b7\",?\"src_rse\":?\"T1_FR_CCIN2P3_Disk\",?\"activity\":?\"Functional?Test\",?\"src_rse_id\":?\"112105749e764d9b8df8f6ca866e4ef8\",?\"request_id\":?\"07ff2b749b7248aba2a907d4315584fd\",?\"request_type\":?\"TRANSFER\",?\"filesize\":?270000000,?\"dest_rse_id\":?\"20f028e6e514453e88f7f2894e86b0ef\",?\"scope\":?\"cms\",?\"dst_rse\":?\"T2_UK_SGrid_RALPP\",?\"src_type\":?\"DISK\",?\"md5\":?\"07d43f0e4ffe60757615eead1c9ea7e0\"}
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; File metadata: {\"dst_type\":?\"DISK\",?\"name\":?\"/store/test/loadtest/source/T1_FR_CCIN2P3_Disk/urandom.270MB.file0000\",?\"adler32\":?\"548de7b7\",?\"src_rse\":?\"T1_FR_CCIN2P3_Disk\",?\"activity\":?\"Functional?Test\",?\"src_rse_id\":?\"112105749e764d9b8df8f6ca866e4ef8\",?\"request_id\":?\"07ff2b749b7248aba2a907d4315584fd\",?\"request_type\":?\"TRANSFER\",?\"filesize\":?270000000,?\"dest_rse_id\":?\"20f028e6e514453e88f7f2894e86b0ef\",?\"scope\":?\"cms\",?\"dst_rse\":?\"T2_UK_SGrid_RALPP\",?\"src_type\":?\"DISK\",?\"md5\":?\"07d43f0e4ffe60757615eead1c9ea7e0\"}
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Job metadata: {\"auth_method\":?\"certificate\",?\"multi_sources\":?false,?\"issuer\":?\"rucio\"}
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Job metadata: {\"auth_method\":?\"certificate\",?\"multi_sources\":?false,?\"issuer\":?\"rucio\"}
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Bringonline token:
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Bringonline token:
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; UDT: 0
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; UDT: 0
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; BDII:lcgbdii.gridpp.rl.ac.uk:2170
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; BDII:lcgbdii.gridpp.rl.ac.uk:2170
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Source token issuer:
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Source token issuer:
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Destination token issuer:
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Destination token issuer:
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Report on the destination tape file: 0
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Report on the destination tape file: 0
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Getting source file size
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Getting source file size
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; File size: 270000000
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; File size: 270000000
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; IPv6: indeterminate
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; IPv6: indeterminate
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; TCP streams: 0
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; TCP streams: 0
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; TCP buffer size: 0
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; TCP buffer size: 0
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Timeout set to: 1115
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; Timeout set to: 1115
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; [1654114749635] BOTH GFAL2:CORE:COPY	LIST:ENTER
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; [1654114749635] BOTH GFAL2:CORE:COPY	LIST:ENTER
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; [1654114749635] BOTH GFAL2:CORE:COPY	LIST:ITEM	srm://ccsrm.in2p3.fr:8443/srm/managerv2?SFN=/pnfs/in2p3.fr/data/cms/disk/data/store/test/loadtest/source/T1_FR_CCIN2P3_Disk/urandom.270MB.file0000 => gsiftp://mover.pp.rl.ac.uk:2811/pnfs/pp.rl.ac.uk/data/cms/store/test/loadtest/source/T1_FR_CCIN2P3_Disk/urandom.270MB.file0000
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; [1654114749635] BOTH GFAL2:CORE:COPY	LIST:ITEM	srm://ccsrm.in2p3.fr:8443/srm/managerv2?SFN=/pnfs/in2p3.fr/data/cms/disk/data/store/test/loadtest/source/T1_FR_CCIN2P3_Disk/urandom.270MB.file0000 => gsiftp://mover.pp.rl.ac.uk:2811/pnfs/pp.rl.ac.uk/data/cms/store/test/loadtest/source/T1_FR_CCIN2P3_Disk/urandom.270MB.file0000
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; [1654114749635] BOTH GFAL2:CORE:COPY	LIST:EXIT
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; [1654114749635] BOTH GFAL2:CORE:COPY	LIST:EXIT
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; [1654114749656] BOTH SRM	PREPARE:ENTER
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; [1654114749656] BOTH SRM	PREPARE:ENTER
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; [1654114749656] SOURCE SRM	CHECKSUM:ENTER
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; [1654114749656] SOURCE SRM	CHECKSUM:ENTER
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; [1654114749697] SOURCE SRM	CHECKSUM:EXIT
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; [1654114749697] SOURCE SRM	CHECKSUM:EXIT
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; [1654114749755] SOURCE GFAL2::PLUGINS::SRM	SRM:GET	Got TURL srm://ccsrm.in2p3.fr:8443/srm/managerv2?SFN=/pnfs/in2p3.fr/data/cms/disk/data/store/test/loadtest/source/T1_FR_CCIN2P3_Disk/urandom.270MB.file0000 => gsiftp://ccdcatli308.in2p3.fr:2811//pnfs/in2p3.fr/data/cms/disk/data/store/test/loadtest/source/T1_FR_CCIN2P3_Disk/urandom.270MB.file0000
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; [1654114749755] SOURCE GFAL2::PLUGINS::SRM	SRM:GET	Got TURL srm://ccsrm.in2p3.fr:8443/srm/managerv2?SFN=/pnfs/in2p3.fr/data/cms/disk/data/store/test/loadtest/source/T1_FR_CCIN2P3_Disk/urandom.270MB.file0000 => gsiftp://ccdcatli308.in2p3.fr:2811//pnfs/in2p3.fr/data/cms/disk/data/store/test/loadtest/source/T1_FR_CCIN2P3_Disk/urandom.270MB.file0000
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; [1654114749755] BOTH SRM	PREPARE:EXIT
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; [1654114749755] BOTH SRM	PREPARE:EXIT
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; [1654114749755] BOTH GFAL2:CORE:COPY	LIST:ENTER
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; [1654114749755] BOTH GFAL2:CORE:COPY	LIST:ENTER
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; [1654114749755] BOTH GFAL2:CORE:COPY	LIST:ITEM	gsiftp://ccdcatli308.in2p3.fr:2811//pnfs/in2p3.fr/data/cms/disk/data/store/test/loadtest/source/T1_FR_CCIN2P3_Disk/urandom.270MB.file0000 => gsiftp://mover.pp.rl.ac.uk:2811/pnfs/pp.rl.ac.uk/data/cms/store/test/loadtest/source/T1_FR_CCIN2P3_Disk/urandom.270MB.file0000
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; [1654114749755] BOTH GFAL2:CORE:COPY	LIST:ITEM	gsiftp://ccdcatli308.in2p3.fr:2811//pnfs/in2p3.fr/data/cms/disk/data/store/test/loadtest/source/T1_FR_CCIN2P3_Disk/urandom.270MB.file0000 => gsiftp://mover.pp.rl.ac.uk:2811/pnfs/pp.rl.ac.uk/data/cms/store/test/loadtest/source/T1_FR_CCIN2P3_Disk/urandom.270MB.file0000
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; [1654114749755] BOTH GFAL2:CORE:COPY	LIST:EXIT
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; [1654114749755] BOTH GFAL2:CORE:COPY	LIST:EXIT
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; [1654114749773] BOTH GSIFTP	TRANSFER:ENTER	([2001:660:5009:9:193:48:99:128]:2811) gsiftp://ccdcatli308.in2p3.fr:2811//pnfs/in2p3.fr/data/cms/disk/data/store/test/loadtest/source/T1_FR_CCIN2P3_Disk/urandom.270MB.file0000 => ([2001:630:58:1c20::82f6:2fea]:2811) gsiftp://mover.pp.rl.ac.uk:2811/pnfs/pp.rl.ac.uk/data/cms/store/test/loadtest/source/T1_FR_CCIN2P3_Disk/urandom.270MB.file0000
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; [1654114749773] BOTH GSIFTP	TRANSFER:ENTER	([2001:660:5009:9:193:48:99:128]:2811) gsiftp://ccdcatli308.in2p3.fr:2811//pnfs/in2p3.fr/data/cms/disk/data/store/test/loadtest/source/T1_FR_CCIN2P3_Disk/urandom.270MB.file0000 => ([2001:630:58:1c20::82f6:2fea]:2811) gsiftp://mover.pp.rl.ac.uk:2811/pnfs/pp.rl.ac.uk/data/cms/store/test/loadtest/source/T1_FR_CCIN2P3_Disk/urandom.270MB.file0000
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; [1654114749773] BOTH GSIFTP	TRANSFER:TYPE	3rd push
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; [1654114749773] BOTH GSIFTP	TRANSFER:TYPE	3rd push
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; [1654114749873] DEST GSIFTP	OVERWRITE	Deleted gsiftp://mover.pp.rl.ac.uk:2811/pnfs/pp.rl.ac.uk/data/cms/store/test/loadtest/source/T1_FR_CCIN2P3_Disk/urandom.270MB.file0000
Line54: INFO    Wed, 01 Jun 2022 21:19:09 +0100; [1654114749873] DEST GSIFTP	OVERWRITE	Deleted gsiftp://mover.pp.rl.ac.uk:2811/pnfs/pp.rl.ac.uk/data/cms/store/test/loadtest/source/T1_FR_CCIN2P3_Disk/urandom.270MB.file0000
Line54: INFO    Wed, 01 Jun 2022 21:19:10 +0100; [1654114750436] DEST GSIFTP	PASV	mover.pp.rl.ac.uk:[2001:630:58:1c20::82f6:2faa]:50190
Line54: INFO    Wed, 01 Jun 2022 21:19:10 +0100; [1654114750436] DEST GSIFTP	PASV	mover.pp.rl.ac.uk:[2001:630:58:1c20::82f6:2faa]:50190
Line54: INFO    Wed, 01 Jun 2022 21:19:10 +0100; [1654114750436] DEST GSIFTP	IPv6	[2001:630:58:1c20::82f6:2faa]:50190
Line54: INFO    Wed, 01 Jun 2022 21:19:10 +0100; [1654114750436] DEST GSIFTP	IPv6	[2001:630:58:1c20::82f6:2faa]:50190
Line54: INFO    Wed, 01 Jun 2022 21:19:13 +0100; bytes: 270000000, avg KB/sec:90921, inst KB/sec:90921, elapsed:3
Line54: INFO    Wed, 01 Jun 2022 21:19:13 +0100; bytes: 270000000, avg KB/sec:90921, inst KB/sec:90921, elapsed:3
Line54: INFO    Wed, 01 Jun 2022 21:19:13 +0100; [1654114753333] BOTH GSIFTP	TRANSFER:EXIT	([2001:660:5009:9:193:48:99:128]:2811) gsiftp://ccdcatli308.in2p3.fr:2811//pnfs/in2p3.fr/data/cms/disk/data/store/test/loadtest/source/T1_FR_CCIN2P3_Disk/urandom.270MB.file0000 => ([2001:630:58:1c20::82f6:2fea]:2811) gsiftp://mover.pp.rl.ac.uk:2811/pnfs/pp.rl.ac.uk/data/cms/store/test/loadtest/source/T1_FR_CCIN2P3_Disk/urandom.270MB.file0000
Line54: INFO    Wed, 01 Jun 2022 21:19:13 +0100; [1654114753333] BOTH GSIFTP	TRANSFER:EXIT	([2001:660:5009:9:193:48:99:128]:2811) gsiftp://ccdcatli308.in2p3.fr:2811//pnfs/in2p3.fr/data/cms/disk/data/store/test/loadtest/source/T1_FR_CCIN2P3_Disk/urandom.270MB.file0000 => ([2001:630:58:1c20::82f6:2fea]:2811) gsiftp://mover.pp.rl.ac.uk:2811/pnfs/pp.rl.ac.uk/data/cms/store/test/loadtest/source/T1_FR_CCIN2P3_Disk/urandom.270MB.file0000
Line54: INFO    Wed, 01 Jun 2022 21:19:13 +0100; [1654114753333] DEST SRM	CLOSE:ENTER	gsiftp://mover.pp.rl.ac.uk:2811/pnfs/pp.rl.ac.uk/data/cms/store/test/loadtest/source/T1_FR_CCIN2P3_Disk/urandom.270MB.file0000
Line54: INFO    Wed, 01 Jun 2022 21:19:13 +0100; [1654114753333] DEST SRM	CLOSE:ENTER	gsiftp://mover.pp.rl.ac.uk:2811/pnfs/pp.rl.ac.uk/data/cms/store/test/loadtest/source/T1_FR_CCIN2P3_Disk/urandom.270MB.file0000
Line54: INFO    Wed, 01 Jun 2022 21:19:13 +0100; [1654114753333] DEST SRM	CLOSE:EXIT	gsiftp://mover.pp.rl.ac.uk:2811/pnfs/pp.rl.ac.uk/data/cms/store/test/loadtest/source/T1_FR_CCIN2P3_Disk/urandom.270MB.file0000
Line54: INFO    Wed, 01 Jun 2022 21:19:13 +0100; [1654114753333] DEST SRM	CLOSE:EXIT	gsiftp://mover.pp.rl.ac.uk:2811/pnfs/pp.rl.ac.uk/data/cms/store/test/loadtest/source/T1_FR_CCIN2P3_Disk/urandom.270MB.file0000
Line54: INFO    Wed, 01 Jun 2022 21:19:13 +0100; [1654114753333] DEST SRM	CHECKSUM:ENTER
Line54: INFO    Wed, 01 Jun 2022 21:19:13 +0100; [1654114753333] DEST SRM	CHECKSUM:ENTER
Line54: INFO    Wed, 01 Jun 2022 21:19:13 +0100; [1654114753468] DEST SRM	CHECKSUM:EXIT
Line54: INFO    Wed, 01 Jun 2022 21:19:13 +0100; [1654114753468] DEST SRM	CHECKSUM:EXIT
Line54: INFO    Wed, 01 Jun 2022 21:19:13 +0100; DESTINATION Source and destination file size matching
Line54: INFO    Wed, 01 Jun 2022 21:19:13 +0100; DESTINATION Source and destination file size matching
Line54: WARNING Wed, 01 Jun 2022 21:19:13 +0100; Timeout stopped
Line54: WARNING Wed, 01 Jun 2022 21:19:13 +0100; Timeout stopped
Line54: INFO    Wed, 01 Jun 2022 21:19:13 +0100; Transfer finished successfully
Line54: INFO    Wed, 01 Jun 2022 21:19:13 +0100; Transfer finished successfully

========= RESTART: C:/Users/Laptop/OneDrive/Documents/stfc/openreadprintfile.py ========
line: 3
line: 15
Line3: INFO    Wed, 01 Jun 2022 21:19:09 +0100; VO: cms
Line15: INFO    Wed, 01 Jun 2022 21:19:09 +0100; User filesize: 270000000

========= RESTART: C:/Users/Laptop/OneDrive/Documents/stfc/openreadprintfile.py ========
what word do you want to find?: VO
what word do you want to find?: User filesize
line: 3
line: 15
Line3: INFO    Wed, 01 Jun 2022 21:19:09 +0100; VO: cms
Line15: INFO    Wed, 01 Jun 2022 21:19:09 +0100; User filesize: 270000000

========= RESTART: C:/Users/Laptop/OneDrive/Documents/stfc/openreadprintfile.py ========
what word do you want to find?: VO
what word do you want to find?: User filesize
line: 3
line: 15
Line54: INFO    Wed, 01 Jun 2022 21:19:13 +0100; Transfer finished successfully
Line54: INFO    Wed, 01 Jun 2022 21:19:13 +0100; Transfer finished successfully

========= RESTART: C:/Users/Laptop/OneDrive/Documents/stfc/openreadprintfile.py ========
what word do you want to find?: VO
what word do you want to find?: User filesize
line: 3
line: 15
Traceback (most recent call last):
  File "C:/Users/Laptop/OneDrive/Documents/stfc/openreadprintfile.py", line 29, in <module>
    if count==num3:
NameError: name 'count' is not defined. Did you mean: 'round'?

========= RESTART: C:/Users/Laptop/OneDrive/Documents/stfc/openreadprintfile.py ========
what word do you want to find?: VO
what word do you want to find?: User filesize
line: 3
line: 15

========= RESTART: C:/Users/Laptop/OneDrive/Documents/stfc/openreadprintfile.py ========
what word do you want to find?: VO
what word do you want to find?: User filesize
line: 3
line: 15

========= RESTART: C:/Users/Laptop/OneDrive/Documents/stfc/openreadprintfile.py ========
what word do you want to find?: VO
what word do you want to find?: User filesize
line: 3
line: 15
Line3: INFO    Wed, 01 Jun 2022 21:19:09 +0100; VO: cms
Line15: INFO    Wed, 01 Jun 2022 21:19:09 +0100; User filesize: 270000000
