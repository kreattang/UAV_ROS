// Auto-generated. Do not edit!

// (in-package rvo.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class Information {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.agent_name = null;
      this.agent_pose_x = null;
      this.agent_pose_y = null;
      this.agent_heading = null;
      this.agent_vel_mag = null;
    }
    else {
      if (initObj.hasOwnProperty('agent_name')) {
        this.agent_name = initObj.agent_name
      }
      else {
        this.agent_name = '';
      }
      if (initObj.hasOwnProperty('agent_pose_x')) {
        this.agent_pose_x = initObj.agent_pose_x
      }
      else {
        this.agent_pose_x = 0.0;
      }
      if (initObj.hasOwnProperty('agent_pose_y')) {
        this.agent_pose_y = initObj.agent_pose_y
      }
      else {
        this.agent_pose_y = 0.0;
      }
      if (initObj.hasOwnProperty('agent_heading')) {
        this.agent_heading = initObj.agent_heading
      }
      else {
        this.agent_heading = 0.0;
      }
      if (initObj.hasOwnProperty('agent_vel_mag')) {
        this.agent_vel_mag = initObj.agent_vel_mag
      }
      else {
        this.agent_vel_mag = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Information
    // Serialize message field [agent_name]
    bufferOffset = _serializer.string(obj.agent_name, buffer, bufferOffset);
    // Serialize message field [agent_pose_x]
    bufferOffset = _serializer.float64(obj.agent_pose_x, buffer, bufferOffset);
    // Serialize message field [agent_pose_y]
    bufferOffset = _serializer.float64(obj.agent_pose_y, buffer, bufferOffset);
    // Serialize message field [agent_heading]
    bufferOffset = _serializer.float64(obj.agent_heading, buffer, bufferOffset);
    // Serialize message field [agent_vel_mag]
    bufferOffset = _serializer.float64(obj.agent_vel_mag, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Information
    let len;
    let data = new Information(null);
    // Deserialize message field [agent_name]
    data.agent_name = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [agent_pose_x]
    data.agent_pose_x = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [agent_pose_y]
    data.agent_pose_y = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [agent_heading]
    data.agent_heading = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [agent_vel_mag]
    data.agent_vel_mag = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.agent_name.length;
    return length + 36;
  }

  static datatype() {
    // Returns string type for a message object
    return 'rvo/Information';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'a69941d7ce3cf8fc435842c1ef18e37d';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string agent_name
    
    float64 agent_pose_x
    float64 agent_pose_y
    float64 agent_heading
    float64 agent_vel_mag
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Information(null);
    if (msg.agent_name !== undefined) {
      resolved.agent_name = msg.agent_name;
    }
    else {
      resolved.agent_name = ''
    }

    if (msg.agent_pose_x !== undefined) {
      resolved.agent_pose_x = msg.agent_pose_x;
    }
    else {
      resolved.agent_pose_x = 0.0
    }

    if (msg.agent_pose_y !== undefined) {
      resolved.agent_pose_y = msg.agent_pose_y;
    }
    else {
      resolved.agent_pose_y = 0.0
    }

    if (msg.agent_heading !== undefined) {
      resolved.agent_heading = msg.agent_heading;
    }
    else {
      resolved.agent_heading = 0.0
    }

    if (msg.agent_vel_mag !== undefined) {
      resolved.agent_vel_mag = msg.agent_vel_mag;
    }
    else {
      resolved.agent_vel_mag = 0.0
    }

    return resolved;
    }
};

module.exports = Information;
