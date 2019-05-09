using System;

namespace WebApplication.Common
{
    [Serializable]
    public class UserLogin
    {
        public string UserName { set; get; }
        public string Password { get; set; }
    }
}
