# root_checker_tool_by_pablo
# أداة التحقق من الروت

هذه أداة بايثون بسيطة للتحقق مما إذا كان جهاز الأندرويد الخاص بك مروّت باستخدام عدة طرق.

## التثبيت

1. قم بتثبيت تطبيق Termux.
2. افتح تطبيق Termux واستخدم الاوامر التالية:
  ```sh
   pkg update && pkg upgrade
   pkg install python
   pkg install git
   git clone https://github.com/Pablo404-EG/root_checker.git
   cd root_check
   python root_check.py
  ```


# اضرار الروت

انعدام الضمان: ترويت الجهاز غالبًا ما يؤدي إلى إلغاء الضمان من الشركة المصنعة، مما يعني أنك قد تفقد دعم الشركة في حال حدوث مشكلة في الجهاز.

المخاطر الأمنية: الروت يمكن أن يجعل جهازك عرضة لهجمات البرامج الضارة والفيروسات، حيث يمكن لهذه البرامج الوصول إلى ملفات النظام الحساسة.

عدم استقرار النظام: قد يؤدي الروت إلى عدم استقرار النظام وتعطل التطبيقات، خاصة إذا قمت بتعديل ملفات النظام أو تثبيت تطبيقات غير متوافقة.

التحديثات التلقائية: الأجهزة المروّتة قد تواجه صعوبة في تلقي التحديثات التلقائية من الشركة المصنعة، مما يعني أنك قد تفوت تحسينات الأمان والميزات الجديدة.

فقدان البيانات: بعض العمليات التي تتطلب الروت قد تؤدي إلى فقدان البيانات أو تلفها إذا لم يتم تنفيذها بشكل صحيح.

# كيفية التخلص من الروت 

إزالة الروت واستعادة الجهاز إلى حالته الأصلية يمكن أن تكون عملية معقدة وتختلف بناءً على الجهاز والإصدار. إليك بعض الطرق العامة لإزالة الروت:

استخدام تطبيق SuperSU:

افتح تطبيق SuperSU.
اذهب إلى "Settings" (الإعدادات).
اختر "Full Unroot" (إزالة الروت بالكامل).
اتبع التعليمات على الشاشة لإكمال العملية.
استخدام تطبيق Magisk:

افتح تطبيق Magisk Manager.
اختر "Uninstall Magisk" (إزالة Magisk).
اختر "Complete Uninstall" (إزالة كاملة).
اتبع التعليمات على الشاشة لإكمال العملية.
إعادة تثبيت النظام الأصلي:

ابحث عن نسخة النظام الأصلية (Stock ROM) لجهازك. يمكنك العثور عليها على مواقع الشركات المصنعة أو المنتديات المتخصصة.
استخدم أداة مثل Odin (لأجهزة Samsung) أو Flash Tool (لأجهزة Sony) لتثبيت النظام الأصلي على جهازك.
تأكد من اتباع التعليمات الخاصة بجهازك بدقة لتجنب أي مشاكل.
إعادة ضبط المصنع:

قد لا يزيل إعادة ضبط المصنع الروت بشكل كامل، لكنه يمكن أن يكون جزءًا من العملية.
اذهب إلى "Settings" (الإعدادات) > "System" (النظام) > "Reset" (إعادة الضبط) > "Factory data reset" (إعادة ضبط المصنع).
