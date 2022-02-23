  @POST("games/{gameId}/like")
  Call<GeneralResponse<ActionResponse>> A(@Header("authorization") String paramString1, @Path("gameId") String paramString2);
  
  @POST("auth/forgot-password")
  Call<GeneralResponse<ForgotPasswordResponse>> a(@Body ForgotPasswordBody paramForgotPasswordBody);
  
  @POST("auth/register")
  Call<RegisterResponse> a(@Body RegisterBody paramRegisterBody);
  
  @POST("auth/reset-password")
  Call<GeneralResponse<PasswordResponse>> a(@Body ResetPasswordBody paramResetPasswordBody);
  
  @POST("auth/sign-in")
  Call<GeneralResponse<SignInResponse>> a(@Body SignInBody paramSignInBody);
  
  @POST("comics/advanced-search")
  Call<GeneralResponse<ComicListResponse>> a(@Header("authorization") String paramString, @Query("page") int paramInt, @Body SortingBody paramSortingBody);
  
  @GET("comics")
  Call<GeneralResponse<ComicListResponse>> a(@Header("authorization") String paramString1, @Query("page") int paramInt, @Query("c") String paramString2, @Query("t") String paramString3, @Query("a") String paramString4, @Query("f") String paramString5, @Query("s") String paramString6, @Query("ct") String paramString7, @Query("ca") String paramString8);
  
  @POST("utils/adjust-exp")
  Call<RegisterResponse> a(@Header("authorization") String paramString, @Body AdjustExpBody paramAdjustExpBody);
  
  @PUT("users/avatar")
  Call<GeneralResponse<PutAvatarResponse>> a(@Header("authorization") String paramString, @Body AvatarBody paramAvatarBody);
  
  @PUT("users/password")
  Call<RegisterResponse> a(@Header("authorization") String paramString, @Body ChangePasswordBody paramChangePasswordBody);
  
  @PUT("users/update-id")
  Call<GeneralResponse> a(@Header("authorization") String paramString, @Body UpdatePicaIdBody paramUpdatePicaIdBody);
  
  @PUT("users/profile")
  Call<RegisterResponse> a(@Header("authorization") String paramString, @Body UpdateProfileBody paramUpdateProfileBody);
  
  @PUT("users/update-qa")
  Call<GeneralResponse> a(@Header("authorization") String paramString, @Body UpdateQandABody paramUpdateQandABody);
  
  @POST("utils/remove-comment")
  Call<GeneralResponse> a(@Header("authorization") String paramString, @Body UserIdBody paramUserIdBody);
  
  @GET("users/favourite")
  Call<GeneralResponse<ComicListResponse>> a(@Header("authorization") String paramString1, @Query("s") String paramString2, @Query("page") int paramInt);
  
  @GET("comics/{comicId}/order/{order}/pages")
  Call<GeneralResponse<ComicPagesResponse>> a(@Header("authorization") String paramString1, @Path("comicId") String paramString2, @Path("order") int paramInt1, @Query("page") int paramInt2);
  
  @POST("comics/{comicId}/comments")
  Call<GeneralResponse<PostCommentResponse>> a(@Header("authorization") String paramString1, @Path("comicId") String paramString2, @Body CommentBody paramCommentBody);
  
  @PUT("users/{userId}/title")
  Call<RegisterResponse> a(@Header("authorization") String paramString1, @Path("userId") String paramString2, @Body UpdateUserTitleBody paramUpdateUserTitleBody);
  
  @GET("comics/leaderboard")
  Call<GeneralResponse<LeaderboardResponse>> a(@Header("authorization") String paramString1, @Query("tt") String paramString2, @Query("ct") String paramString3);
  
  @GET("init?platform=android")
  Call<GeneralResponse<InitialResponse>> ak(@Header("authorization") String paramString);
  
  @GET("categories")
  Call<GeneralResponse<CategoryResponse>> al(@Header("authorization") String paramString);
  
  @GET("users/profile")
  Call<GeneralResponse<UserProfileResponse>> am(@Header("authorization") String paramString);
  
  @POST("users/punch-in")
  Call<GeneralResponse<PunchInResponse>> an(@Header("authorization") String paramString);
  
  @GET("comics/random")
  Call<GeneralResponse<ComicRandomListResponse>> ao(@Header("authorization") String paramString);
  
  @GET("comics/knight-leaderboard")
  Call<GeneralResponse<LeaderboardKnightResponse>> ap(@Header("authorization") String paramString);
  
  @GET("collections")
  Call<GeneralResponse<CollectionsResponse>> aq(@Header("authorization") String paramString);
  
  @GET("keywords")
  Call<GeneralResponse<KeywordsResponse>> ar(@Header("authorization") String paramString);
  
  @GET("banners")
  Call<GeneralResponse<BannersResponse>> as(@Header("authorization") String paramString);
  
  @GET("chat")
  Call<GeneralResponse<ChatroomListResponse>> at(@Header("authorization") String paramString);
  
  @GET("pica-apps")
  Call<GeneralResponse<PicaAppsResponse>> au(@Header("authorization") String paramString);
  
  @GET("applications?platform=android")
  Call<GeneralResponse<ApplicationsResponse>> b(@Header("authorization") String paramString, @Query("page") int paramInt);
  
  @POST("utils/block-user")
  Call<GeneralResponse> b(@Header("authorization") String paramString, @Body UserIdBody paramUserIdBody);
  
  @GET("comics/{comicId}/eps")
  Call<GeneralResponse<ComicEpisodeResponse>> b(@Header("authorization") String paramString1, @Path("comicId") String paramString2, @Query("page") int paramInt);
  
  @POST("comments/{commentId}")
  Call<GeneralResponse<PostCommentResponse>> b(@Header("authorization") String paramString1, @Path("commentId") String paramString2, @Body CommentBody paramCommentBody);
  
  @GET("users/my-comments")
  Call<GeneralResponse<ProfileCommentsResponse>> c(@Header("authorization") String paramString, @Query("page") int paramInt);
  
  @GET("comics/{comicId}/comments")
  Call<GeneralResponse<CommentsResponse>> c(@Header("authorization") String paramString1, @Path("comicId") String paramString2, @Query("page") int paramInt);
  
  @POST("games/{gameId}/comments")
  Call<GeneralResponse<PostCommentResponse>> c(@Header("authorization") String paramString1, @Path("gameId") String paramString2, @Body CommentBody paramCommentBody);
  
  @GET("users/notifications")
  Call<GeneralResponse<NotificationsResponse>> d(@Header("authorization") String paramString, @Query("page") int paramInt);
  
  @GET("comments/{commentId}/childrens")
  Call<GeneralResponse<CommentsResponse>> d(@Header("authorization") String paramString1, @Path("commentId") String paramString2, @Query("page") int paramInt);
  
  @GET("init")
  Call<WakaInitResponse> dM();
  
  @GET("games")
  Call<GeneralResponse<GameListResponse>> e(@Header("authorization") String paramString, @Query("page") int paramInt);
  
  @GET("eps/{epsId}/pages")
  Call<GeneralResponse<ComicPagesResponse>> e(@Header("authorization") String paramString1, @Path("epsId") String paramString2, @Query("page") int paramInt);
  
  @GET("announcements")
  Call<GeneralResponse<AnnouncementsResponse>> f(@Header("authorization") String paramString, @Query("page") int paramInt);
  
  @GET("games/{gameId}/comments")
  Call<GeneralResponse<CommentsResponse>> f(@Header("authorization") String paramString1, @Path("gameId") String paramString2, @Query("page") int paramInt);
  
  @POST("users/{userId}/dirty")
  Call<GeneralResponse<UserProfileDirtyResponse>> p(@Header("authorization") String paramString1, @Path("userId") String paramString2);
  
  @GET("users/{userId}/profile")
  Call<GeneralResponse<UserProfileResponse>> q(@Header("authorization") String paramString1, @Path("userId") String paramString2);
  
  @GET("comics/{comicId}")
  Call<GeneralResponse<ComicDetailResponse>> r(@Header("authorization") String paramString1, @Path("comicId") String paramString2);
  
  @POST("comics/{comicId}/like")
  Call<GeneralResponse<ActionResponse>> s(@Header("authorization") String paramString1, @Path("comicId") String paramString2);
  
  @POST("comics/{comicId}/favourite")
  Call<GeneralResponse<ActionResponse>> t(@Header("authorization") String paramString1, @Path("comicId") String paramString2);
  
  @GET("comics/{comicId}/recommendation")
  Call<GeneralResponse<ComicRandomListResponse>> u(@Header("authorization") String paramString1, @Path("comicId") String paramString2);
  
  @POST("comments/{commentId}/like")
  Call<GeneralResponse<ActionResponse>> v(@Header("authorization") String paramString1, @Path("commentId") String paramString2);
  
  @POST("comments/{commentId}/hide")
  Call<GeneralResponse<MessageResponse>> w(@Header("authorization") String paramString1, @Path("commentId") String paramString2);
  
  @POST("comments/{commentId}/report")
  Call<GeneralResponse<MessageResponse>> x(@Header("authorization") String paramString1, @Path("commentId") String paramString2);
  
  @POST("comments/{commentId}/top")
  Call<GeneralResponse<CommentPostToTopResponse>> y(@Header("authorization") String paramString1, @Path("commentId") String paramString2);
  
  @GET("games/{gameId}")
  Call<GeneralResponse<GameDetailResponse>> z(@Header("authorization") String paramString1, @Path("gameId") String paramString2);