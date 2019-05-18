
(cl:in-package :asdf)

(defsystem "ros_learning-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "AddTwoints" :depends-on ("_package_AddTwoints"))
    (:file "_package_AddTwoints" :depends-on ("_package"))
    (:file "WordCount" :depends-on ("_package_WordCount"))
    (:file "_package_WordCount" :depends-on ("_package"))
  ))