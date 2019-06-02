; Auto-generated. Do not edit!


(cl:in-package rvo-msg)


;//! \htmlinclude Information.msg.html

(cl:defclass <Information> (roslisp-msg-protocol:ros-message)
  ((agent_name
    :reader agent_name
    :initarg :agent_name
    :type cl:string
    :initform "")
   (agent_pose_x
    :reader agent_pose_x
    :initarg :agent_pose_x
    :type cl:float
    :initform 0.0)
   (agent_pose_y
    :reader agent_pose_y
    :initarg :agent_pose_y
    :type cl:float
    :initform 0.0)
   (agent_heading
    :reader agent_heading
    :initarg :agent_heading
    :type cl:float
    :initform 0.0)
   (agent_vel_mag
    :reader agent_vel_mag
    :initarg :agent_vel_mag
    :type cl:float
    :initform 0.0))
)

(cl:defclass Information (<Information>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Information>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Information)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name rvo-msg:<Information> is deprecated: use rvo-msg:Information instead.")))

(cl:ensure-generic-function 'agent_name-val :lambda-list '(m))
(cl:defmethod agent_name-val ((m <Information>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader rvo-msg:agent_name-val is deprecated.  Use rvo-msg:agent_name instead.")
  (agent_name m))

(cl:ensure-generic-function 'agent_pose_x-val :lambda-list '(m))
(cl:defmethod agent_pose_x-val ((m <Information>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader rvo-msg:agent_pose_x-val is deprecated.  Use rvo-msg:agent_pose_x instead.")
  (agent_pose_x m))

(cl:ensure-generic-function 'agent_pose_y-val :lambda-list '(m))
(cl:defmethod agent_pose_y-val ((m <Information>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader rvo-msg:agent_pose_y-val is deprecated.  Use rvo-msg:agent_pose_y instead.")
  (agent_pose_y m))

(cl:ensure-generic-function 'agent_heading-val :lambda-list '(m))
(cl:defmethod agent_heading-val ((m <Information>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader rvo-msg:agent_heading-val is deprecated.  Use rvo-msg:agent_heading instead.")
  (agent_heading m))

(cl:ensure-generic-function 'agent_vel_mag-val :lambda-list '(m))
(cl:defmethod agent_vel_mag-val ((m <Information>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader rvo-msg:agent_vel_mag-val is deprecated.  Use rvo-msg:agent_vel_mag instead.")
  (agent_vel_mag m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Information>) ostream)
  "Serializes a message object of type '<Information>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'agent_name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'agent_name))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'agent_pose_x))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'agent_pose_y))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'agent_heading))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'agent_vel_mag))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Information>) istream)
  "Deserializes a message object of type '<Information>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'agent_name) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'agent_name) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'agent_pose_x) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'agent_pose_y) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'agent_heading) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'agent_vel_mag) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Information>)))
  "Returns string type for a message object of type '<Information>"
  "rvo/Information")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Information)))
  "Returns string type for a message object of type 'Information"
  "rvo/Information")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Information>)))
  "Returns md5sum for a message object of type '<Information>"
  "a69941d7ce3cf8fc435842c1ef18e37d")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Information)))
  "Returns md5sum for a message object of type 'Information"
  "a69941d7ce3cf8fc435842c1ef18e37d")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Information>)))
  "Returns full string definition for message of type '<Information>"
  (cl:format cl:nil "string agent_name~%~%float64 agent_pose_x~%float64 agent_pose_y~%float64 agent_heading~%float64 agent_vel_mag~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Information)))
  "Returns full string definition for message of type 'Information"
  (cl:format cl:nil "string agent_name~%~%float64 agent_pose_x~%float64 agent_pose_y~%float64 agent_heading~%float64 agent_vel_mag~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Information>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'agent_name))
     8
     8
     8
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Information>))
  "Converts a ROS message object to a list"
  (cl:list 'Information
    (cl:cons ':agent_name (agent_name msg))
    (cl:cons ':agent_pose_x (agent_pose_x msg))
    (cl:cons ':agent_pose_y (agent_pose_y msg))
    (cl:cons ':agent_heading (agent_heading msg))
    (cl:cons ':agent_vel_mag (agent_vel_mag msg))
))
