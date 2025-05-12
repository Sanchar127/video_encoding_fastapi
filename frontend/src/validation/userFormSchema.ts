
import * as yup from 'yup'

export const userSchema = yup.object({
  name: yup.string().required('Name is required').min(2, 'Name must be at least 2 characters'),
  email: yup.string().email('Invalid email format').required('Email is required'),
  password: yup
    .string()
    .required('Password is required')
    .min(8, 'Password must be at least 8 characters')
    .matches(/[a-z]/, 'Must contain a lowercase letter')
    .matches(/[A-Z]/, 'Must contain an uppercase letter')
    .matches(/\d/, 'Must contain a number')
    .matches(/[@$!%*#?&]/, 'Must contain a special character'),
  mobile: yup.string().required('Mobile number is required').matches(/^[6-9]\d{9}$/, 'Invalid mobile number'),
  address: yup.string().required('Address is required').min(5, 'Address must be at least 5 characters'),
  callback_key: yup.string().required('Callback Key is required'),
  callback_url: yup.string().required('Callback URL is required').url('Must be a valid URL'),
  callback_secret_key: yup.string().required('Callback Secret Key is required'),
  role: yup.string().required('Role is required').oneOf(['admin', 'user', 'super_admin'], 'Invalid role'),
})
